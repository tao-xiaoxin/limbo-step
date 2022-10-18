'''
小米运动定时任务
'''
import time
from applications.extensions.init_mysql import cursor, db, get_result, update_result
from applications.libs import mi_login, zepp_life, send_push


def mi_task():
    sql1 = '''
    SELECT PHONE,PASSWORD,USER_ID,SCOPE FROM file_user2account 
    ORDER BY USER_ID ASC
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
        new_phone = phone.replace(row1[0][3:7], 'xxxx')
        row_dict = {"phone": phone, "pwd": pwd, "user_id": user_id,
                    "gte": gte, "lte": lte,
                    "sync_results": f"账号{new_phone}:今日修改步数 **{step}** " + response['message']}

        # 记录同步结果
        update_result(
            """
            INSERT INTO file_task_log (TIME_STAMP,USER_ID, TASK_TYPE,CONTENT) VALUES ({},'{}','{}','{}')
            """.format(int(time.time()), user_id,
                       '小米运动',
                       f"账号{phone} 今日修改步数:{step} " + response['message'], ))
        if str(user_id) not in user_dict:
            user_dict.update(**{f"{user_id}": [row_dict]})
        else:
            user_dict[f'{user_id}'].append(row_dict)
    for row2 in get_result(
            '''
            SELECT APP_ID,UID FROM file_user2push
            '''):
        uid = str(row2[1])
        if uid not in user_dict:
            continue
        # 将结果推送给微信订阅
        acc_list = [d['sync_results'] for d in user_dict[uid]]
        send_result = send_push(row2[0], "今日步数结果推送", "今日运动结果为:<br>{}".format(str.join("<br>", acc_list)))
        # 将推送失败的改为掉线
        if send_result["code"] != 200:
            update_result(
                '''
                UPDATE file_user2push SET IS_ACTIVATE = 0 WHERE APP_ID = {}
                '''.format(row2[0]))
        time.sleep(1)
        print("今日步数结果推送,"+"今日运动结果为:<br>{}".format(str.join("<br>", acc_list)))
