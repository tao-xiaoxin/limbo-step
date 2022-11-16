from flask import Blueprint, render_template, request
from utils.response import fail_api, success_api
from utils.sync_step import sync_step
from utils.operation_csv import write_csv
from utils.log import logger

index_bp = Blueprint('Index', __name__, url_prefix='/')


@index_bp.route('/')
def index():
    return render_template('index/index.html')


@index_bp.route('/login')
def login():
    return render_template('login/login.html')


# 登录
@index_bp.post('/login')
def login_post():
    data = request.form
    user = data.get('user')
    password = data.get('password')
    scope = data.get('scope')
    if not user:
        return fail_api(msg="账号不可以为空奥!")
    if not password:
        return fail_api(msg="账号不可以为空奥!")
    if "~" not in scope or len((str(scope).split('~'))) != 2:
        return fail_api(msg="请检查刷步范围,必须使用英文~连接!")
    try:
        gte, lte = (str(scope).split('~'))[0], (str(scope).split('~'))[-1]
    except Exception as e:
        logger.error(e)
        return fail_api(msg="步数范围必须是数字!")
    if lte <= gte:
        return fail_api(msg="步数范围必须开始值小于结束值!")
    msg, step = sync_step(user=user, pwd=password, gte=gte, lte=lte)
    account = user.replace(user[3:7], '****')
    s_data = [{"user": user, "password": password,
               "gte": gte, "lte": lte, }]
    try:
        # 将账号保存到csv中
        write_csv(data=s_data)
    except Exception as e:
        logger.error(e)
        return fail_api(msg="账号信息保存出错,请联系开发者调试!")
    return success_api(msg=f"账号:{account},刷步{step}{msg}")
