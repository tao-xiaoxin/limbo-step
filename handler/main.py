import datetime, time, bson, os
from configs.config import configs as settings
from utils.operation_csv import read_csv, write_csv
from utils.log import logger as logging
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from libs.pushplus import send
from utils.sync_step import sync_step

executors = {
    'default': ThreadPoolExecutor(5)
}
scheduler = BlockingScheduler(timezone='Asia/Shanghai', executors=executors)


def get_time():
    '''
    获取当前时间
    :return:
    '''
    now_time = datetime.datetime.now()
    now_date = now_time.strftime('%Y%m%d')
    time_str = now_time.strftime("%Y%m%d%H%M")
    return now_date, time_str


def save_fail(s_fail):
    '''
    保存处理失败的账号
    :param s_fail:
    :return:
    '''
    now_date, time_str = get_time()
    file_path = 'logs/{}/{}/{}.csv'.format(now_date, 'is_fail', time_str)
    write_csv(file_path=file_path, data=s_fail)


def save_success(s_success):
    '''
    保存处理成功的
    :param s_success:
    :return:
    '''
    now_date, time_str = get_time()
    file_path = 'logs/{}/{}/{}.csv'.format(now_date, 'is_success', time_str)
    write_csv(file_path=file_path, data=s_success)


def main():
    '''
    主要的逻辑
    :return:
    '''
    s_fail = list()
    s_success = list()
    s_result = list()
    for index, values in read_csv():
        msg, step = sync_step(values.user, values.password, values.gte, values.lte)
        time.sleep(15)
        account = values.user.replace(values.user[3:7], '****')
        result = f"当前用户：**{account}** 修改步数：**{step}** 修改结果: " + msg
        data_dict = {
            "user": values.user,
            "password": values.password,
            "gte": values.gte,
            "lte": values.lte,
        }
        s_result.append(result)
        if msg == "提交失败!":
            s_fail.append(data_dict)
            continue
        s_success.append(data_dict)
    send_result = send.plus_send(msg=str.join("<br>", s_result))
    if not send_result:
        logging.error('推送结果失败!')
    return s_success, s_fail


def job():
    '''
    定时任务入口
    :return:
    '''

    s_success, s_fail = main()
    # save_fail(s_fail)
    # save_success(s_success)
    logging.info("当前任务执行完成")


def run():
    # 每天
    scheduler.add_job(job, 'cron', hour=8, minute=8, )
    scheduler.add_job(job, 'cron', hour=10, minute=10, )
    scheduler.add_job(job, 'cron', hour=12, minute=12, )
    scheduler.add_job(job, 'cron', hour=15, minute=15, )
    scheduler.add_job(job, 'cron', hour=17, minute=17, )
    scheduler.add_job(job, 'cron', hour=19, minute=19, )
    scheduler.add_job(job, 'cron', hour=21, minute=21, )
    # nohup python3 run.py >nohup.out 2>&1 &
    # scheduler.add_job(mi_job, 'interval', seconds=10)
    logging.info("**LIMBO-STEP-TASK-START**")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown(wait=False)


# # 阿里云函数
def handler(*args):
    run()


if __name__ == '__main__':
    run()
