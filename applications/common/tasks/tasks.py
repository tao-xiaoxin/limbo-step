from applications.extensions.init_mysql import cursor, db, get_result, update_result
from applications.libs import mi_login, zepp_life, send_push
from applications.models.admin_user import *

task_list = ['task2', 'task3', 'task4', "mi_job"]


def task2(a, b):
    print(f'定时任务_1_{a},{b},{datetime.datetime.now()}')


def task3(a, b):
    print(f'定时任务_2_{a}{b}{datetime.datetime.now()}')


def task4(a, b):
    print(f'定时任务_4_{a}{b}{datetime.datetime.now()}')


def mi_job(c, d):
    '''
    小米运动定时任务
    '''
    sql1 = '''
    select phone,password,user_id,scope from file_user2account 
    order by user_id asc
    '''
    result1 = get_result(sql1)
    user_dict = dict()
    for row1 in list(result1):
        phone = row1[0]
        pwd = row1[1]
        user_id = row1[2]
        scope = str(row1[3]).split('~')
        gte = int(scope[0])
        lte = int(scope[-1])
        '''
        开始刷步数
        '''
        login_token, uid = mi_login.login(phone, pwd)
        step, response = zepp_life.zepp_step(login_token, uid, gte, lte)

        row_dict = {"phone": phone, "pwd": pwd, "user_id": user_id,
                    "gte": gte, "lte": lte,
                    "sync_results": f"账号{phone}:今日修改步数（{step}）[" + response['message'] + "]"}
        # 记录同步结果

        # 如果同步不成功改为掉线
        acc_code = response["code"]
        if acc_code != 200:
            update_result(
                '''
                UPDATE file_user2account SET is_activate = 0 WHERE phone = {} 
                '''.format(phone))
        if str(user_id) not in user_dict:
            user_dict.update(**{f"{user_id}": [row_dict]})
        else:
            user_dict[f'{user_id}'].append(row_dict)
    result2 = get_result(
        '''
        select app_id,uid from file_user2push
        ''')
    for row2 in result2:
        uid = str(row2[1])
        if uid not in user_dict:
            continue
        # 将结果推送给微信订阅
        send_push(row2[0], "今日运动步数为...", "今日运动结果为:{}".format(user_dict[uid]))
