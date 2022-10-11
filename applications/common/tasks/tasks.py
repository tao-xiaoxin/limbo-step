from applications.extensions.init_mysql import cursor, db, get_result, update_result
from applications.libs import mi_login, zepp_life, send_push
from applications.models.admin_user import *
import time

task_list = ['task2', 'task3', 'task4']


def task2(a, b):
    print(f'定时任务_1_{a},{b},{datetime.datetime.now()}')


def task3(a, b):
    print(f'定时任务_2_{a}{b}{datetime.datetime.now()}')


def task4(a, b):
    print(f'定时任务_4_{a}{b}{datetime.datetime.now()}')


