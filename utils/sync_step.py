from random import randint
from libs.mi.other import *


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
