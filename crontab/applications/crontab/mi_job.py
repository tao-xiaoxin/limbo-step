'''
小米运动定时任务
'''
from email.mime import application
import time
from random import randint
from applications.common.init_log import logger as logging
from applications.lib import send_push
from applications.lib.mi.other_sdk import *
from applications.models import *




def random_step(gte, lte):
    try:
        return str(randint(int(gte), int(lte)))
    except:
        return lte


def sync_step(user, pwd, gte, lte):
    msg = "提交失败!"
    step = random_step(gte, lte)
    if reserve_step1(user, pwd, step):
        msg = "提交成功!"
    elif reserve_step2(user, pwd, step):
        msg = "提交成功!"
    else:
        if email_step(user, pwd, step):
            msg = "提交成功!"
    return msg, step


def mi_job():
    fail_list = list()
    user_dict = dict()
    row_dict = dict()
    o_user2account=User2Account.objects.values('phone',"password","user_id","scope")
    for qs in o_user2account:
        user =qs['phone']
        pwd = qs["password"]
        user_id = qs["user_id"]
        scope = str(qs["scope"]).split('~')
        msg, step = sync_step(user, pwd,scope[0],scope[-1])
        time.sleep(15)
        account = user.replace(user[3:7], '****')
        result = f"当前用户：**{account}** 修改步数：**{step}** 修改结果: " + msg
        if user_id not in row_dict:
            row_dict[user_id]=[result]
        else:
            row_dict[user_id].append(result)
        # 记录同步结果
        FileTaskLog.objects.create(user_id=user_id,time_stamp=int(time.time()),task_type='小米运动',
                                    content=result,)
    o_user2push=FileUser2Push.objects.values("app_id",'uid')
    for u in o_user2push:
        # if str(u['uid']) !="1":
        #     continue
        # 将结果推送给微信订阅
        try:
            send_msg='<br>'.join(row_dict[u['uid']])
            send_result = send_push(u['app_id'], "今日步数结果推送", "今日运动结果为:<br>{}".format(send_msg))
        except Exception as e:
            logging.error(e)
    logging.info('当前任务已经完成！')