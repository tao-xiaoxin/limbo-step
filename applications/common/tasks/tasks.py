import datetime
from applications.models.admin_user import *

from applications.extensions import db
from sqlalchemy import func
task_list = ['task2', 'task3', 'task4',"mi_job"]


def task2(a, b):
    print(f'定时任务_1_{a},{b},{datetime.datetime.now()}')


def task3(a, b):
    print(f'定时任务_2_{a}{b}{datetime.datetime.now()}')


def task4(a, b):
    print(f'定时任务_4_{a}{b}{datetime.datetime.now()}')
