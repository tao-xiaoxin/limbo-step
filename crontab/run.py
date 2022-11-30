'''
定时任务启动调度器入口
'''
import os
import django
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'limbo_step_task.settings')
django.setup()
from applications.models import *
from applications.common.init_log import logger as logging
from applications.crontab.mi_job import mi_job
executors = {
    'default': ThreadPoolExecutor(5)
}
scheduler = BlockingScheduler(timezone='Asia/Shanghai', executors=executors)


def run():
    mi_job()
    # scheduler.add_job(mi_job, 'cron', hour=8, minute=8, )
    # scheduler.add_job(mi_job, 'cron', hour=9, minute=24,)
    # scheduler.add_job(mi_job, 'cron', hour=10, minute=8, )
    # scheduler.add_job(mi_job, 'cron', hour=12, minute=8, )
    # scheduler.add_job(mi_job, 'cron', hour=15, minute=8, )
    # scheduler.add_job(mi_job, 'cron', hour=19, minute=8, )
    # nohup python3 run.py >nohup.out 2>&1 &
    # scheduler.add_job(mi_job, 'interval', seconds=10)
    # logging.info("**LIMBO-STEP-TASK-START**")
    # try:
    #     scheduler.start()
    # except (KeyboardInterrupt, SystemExit):
    #     scheduler.shutdown(wait=False)


if __name__ == '__main__':
    run()