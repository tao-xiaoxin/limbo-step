'''
小米运动定时任务
'''
import time
from applications.common.init_log import logger as logging
from applications.lib import mi_login, zepp_life, send_push
from applications.models import *

def check():
  print("hello django-crontab")


def mi_job():
    user_dict = dict()
    o_user2account=User2Account.objects.values('phone',"password","user_id","scope")
    for qs in o_user2account:
        phone =qs['phone']
        pwd = qs["password"]
        user_id = qs["user_id"]
        scope = str(qs["scope"]).split('~')
        gte = int(scope[0])
        lte = int(scope[-1])
        '''
        开始刷步数
        '''
        login_token, uid = mi_login.login(phone, pwd)
        step, response = zepp_life.zeep_step(login_token, uid, gte, lte)
        message = response['message']
        if str(message) != "success":
            message = "失败！"
        new_phone = phone.replace(phone[3:7], 'xxxx')
        row_dict = {"phone": phone, "pwd": pwd, "user_id": user_id,
                    "gte": gte, "lte": lte,
                    "sync_results": f"账号{new_phone}:今日修改步数 **{step}** " + message}
        # 记录同步结果
        FileTaskLog.objects.create(user_id=user_id,time_stamp=int(time.time()),task_type='小米运动',
                                    content=f"账号{phone} 今日修改步数:{step} " + response['message'],)

        if str(user_id) not in user_dict:
            user_dict.update(**{f"{user_id}": [row_dict]})
        else:
            user_dict[f'{user_id}'].append(row_dict)
        time.sleep(0.1)
    o_user2push=FileUser2Push.objects.values("app_id",'uid')
    for u in o_user2push:
        # if str(u['uid']) !="1":
        #     continue
        # 将结果推送给微信订阅
        acc_list = [d['sync_results'] for d in user_dict[str(u['uid'])]]
        logging.info(acc_list)
        send_result = send_push(u['app_id'], "今日步数结果推送", "今日运动结果为:<br>{}".format(str.join("<br>", acc_list)))
        # 将推送失败的改为掉线
        if send_result["code"] != 200:
            FileUser2Push.objects.filter(app_id=u['uid']).update(is_activate=1)
    print("complete!")