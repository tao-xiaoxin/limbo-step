'''
定时任务启动入口
'''
from apscheduler.schedulers.blocking import BlockingScheduler
from applications.crontab.mi_job import mi_task

scheduler = BlockingScheduler()


def run():
    scheduler.add_job(mi_task, 'cron', hour=8, minute=8,timezone='Asia/Shanghai',)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown(wait=False)


if __name__ == '__main__':
    run()
