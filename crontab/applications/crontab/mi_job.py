'''
小米运动定时任务
'''
from email.mime import application
import time,random
from applications.common.init_log import logger as logging
from applications.lib import mi_login, zepp_life, send_push
from applications.lib.mi.other_sdk import pig_step,phone_step,email_step
from applications.models import *

def random_step(gte,lte):
    return int(random.randint(gte,lte))

def generate_code(qs,code_list):
  '''
  开始刷步
  '''
  phone =qs['phone']
  pwd = qs["password"]
  scope = str(qs["scope"]).split('~')
  step=random_step(int(scope[0]),int(scope[-1]))
  # try:
  #     login_token, uid = mi_login.login(phone, pwd)
  #     step, response = zepp_life.zeep_step(login_token, uid,step)
  #     code_list.append({"code":response['code'],"msg":response['message'],"step":step})
  # except Exception as e:
  #   logging.error(e)
  try:
    step,response=pig_step(phone,pwd,step)
    code_list.append({"code":response['code'],"msg":response['msg'],"step":step})
  except Exception as e:
    logging.error(e)
  try:
    step,response=phone_step(phone,pwd,step)
    code_list.append({"code":response['code'],"msg":response['msg'],"step":step})
  except Exception as e:
    logging.error(e)
  try:
    step,response=email_step(phone,pwd,step)
    code_list.append({"code":response['code'],"msg":response['msg'],"step":step})
  except Exception as e:
    logging.error(e)
  return code_list

def check_code(code_list):
  data_dict = {"step": 0, "msg": 'failure',"code":201}
  for d in code_list:
      code = d['code']
      if not d or code == 0:
        continue
      elif code == 200 and int(data_dict['step']) <= int(d['step']):
        step = int(d["step"])
        msg = "提交成功!"
        code =200
        data_dict.update(**{"step": step, "msg": msg})
        continue
      elif '提交成功!' in data_dict.values():
        continue
      elif code ==200:
        step = int(d["step"])
        msg = "提交成功!"
        code =200
        data_dict.update(**{"step": step, "msg": msg})
        continue
      step = int(d["step"])
      msg = "failure!"
      data_dict.update(**{"step": step, "msg": msg})
  return data_dict

def mi_job():
    fail_list = list()
    user_dict = dict()
    o_user2account=User2Account.objects.values('phone',"password","user_id","scope")
    for qs in o_user2account:
        code_list =list()
        phone =qs['phone']
        pwd = qs["password"]
        user_id = qs["user_id"]
        scope = str(qs["scope"]).split('~')
        gte = int(scope[0])
        lte = int(scope[-1])
        # 提交刷步
        code_list=generate_code(qs,code_list)
        # 清洗刷步数据
        data_dict = check_code(code_list)
        new_phone = phone.replace(phone[3:7], 'xxxx')
        message=data_dict['msg']
        step=data_dict['step']
        code = data_dict['code']
        row_dict = {"phone": phone, "pwd": pwd, "user_id": user_id,
                    "gte": gte, "lte": lte,
                    "sync_results": f"账号{new_phone}:今日修改步数 **{step}** " + message}
        if '提交成功' not in row_dict['sync_results']:
          fail_list.append(row_dict)
          logging.info(row_dict)
        logging.info(row_dict)
        # 改为掉线
        # if code !=200:
        #   User2Account.objects.filter(phone=phone).update(is_activate=0)
        # 记录同步结果
        FileTaskLog.objects.create(user_id=user_id,time_stamp=int(time.time()),task_type='小米运动',
                                    content=f"账号{phone} 今日修改步数:{step} " + message,)

        if str(user_id) not in user_dict:
            user_dict.update(**{f"{user_id}": [row_dict]})
        else:
            user_dict[f'{user_id}'].append(row_dict)
        time.sleep(15)
    logging.error(fail_list)
    o_user2push=FileUser2Push.objects.values("app_id",'uid')
    for u in o_user2push:
        if str(u['uid']) !="1":
            continue
        # 将结果推送给微信订阅
        acc_list = [d['sync_results'] for d in user_dict[str(u['uid'])]]
        logging.info(acc_list)
        send_result = send_push(u['app_id'], "今日步数结果推送", "今日运动结果为:<br>{}".format(str.join("<br>", acc_list)))
        # 将推送失败的改为掉线
        if send_result["code"] != 200:
            FileUser2Push.objects.filter(app_id=u['uid']).update(is_activate=1)
    print("complete!")