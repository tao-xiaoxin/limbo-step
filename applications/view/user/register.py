from applications import models
import re, requests
from flask import Blueprint, session, redirect, url_for, render_template, request
from flask_login import current_user, login_user, login_required, logout_user
from sqlalchemy import or_, and_, not_
from applications.common import admin as index_curd
from applications.common.admin_log import login_log
from applications.common.utils.http import fail_api, success_api
from applications.models import User
from applications.libs.briefly.briefly import get_briefly
from applications.libs import get_briefly, get_conclusion
from applications.configs import BaseConfig as configs

config = configs()
user_register = Blueprint('user_register', __name__, url_prefix='/user/register')


# 用户注册
@user_register.route('/')
def index():
    # 当前用户
    if current_user.is_authenticated:
        return redirect(url_for('user_admin.index'))
    return render_template('user/register/index.html')


# 注册
@user_register.post('/')
def register_post():
    req = request.form
    print(req)
    email = req.get('email')
    password = req.get('password')
    username = req.get('username')
    code = req.get('captcha').__str__().lower()
    if not (3 >= len(username) <= 18):
        return fail_api(msg="用户名长度在3~18之间!")
    if not email or not password or not username or not code or not re.match(
            r'^[0-9a-za-z_]{0,19}@[0-9a-za-z]{1,13}\.[com,cn,net]{1,3}$', email):
        return fail_api(msg="请输入正确的邮箱账号用户名或者密码!")
    if not re.match(
            r'^(?![a-zA-Z]+$)(?![A-Z0-9]+$)(?![A-Z\W_]+$)(?![a-z0-9]+$)(?![a-z\W_]+$)(?![0-9\W_]+$)[a-zA-Z0-9\W_]{8,18}$',
            password) or not (18 <= len(password) >= 8):
        return fail_api(msg="密码必须要包含大写字母,小写字母,数字,特殊字符(至少三种),且长度在8~18之间!")
    s_code = session.get("code", None)
    session["code"] = None
    if not all([code, s_code]):
        return fail_api(msg="参数错误")
    if code != s_code:
        return fail_api(msg="验证码错误")
    if bool(User.query.filter_by(email=email).count()):
        return fail_api(msg="用户已经存在")
    # 开启百度内容审核验证
    if config.BAIDU_POWER:
        get_conclusion(username)
    # 每日一言
    remark = str(get_briefly()).split("/")[-1]
    # user = User(username=username, email=email, remark=remark)
    # user.set_password(password)
    # db.session.add(user)
    # db.session.commit()
    # # 注册成功后直接登录后台
    # # 登录
    # login_user(user)
    # # 记录登录日志
    # login_log(request, uid=user.id, is_access=True)
    # # 存入权限
    # index_curd.add_auth_session()
    return success_api(msg="注册成功!")
