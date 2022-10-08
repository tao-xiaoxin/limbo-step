import datetime
from applications.models.admin_user import *
from applications.libs import mi_login,zepp_life,send_push
task_list = ['task2', 'task3', 'task4',"mi_job"]


def task2(a, b):
    print(f'定时任务_1_{a},{b},{datetime.datetime.now()}')


def task3(a, b):
    print(f'定时任务_2_{a}{b}{datetime.datetime.now()}')


def task4(a, b):
    print(f'定时任务_4_{a}{b}{datetime.datetime.now()}')

def mi_job():
    '''
    小米运动定时任务
    '''
    ...
