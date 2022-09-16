import re
from flask import Blueprint, session, redirect, url_for, render_template, request
from flask_login import current_user, login_user, login_required, logout_user
from sqlalchemy import or_, and_, not_
from applications.common import admin as index_curd
from applications.common.admin_log import login_log
from applications.common.utils.http import fail_api, success_api
from applications.models import User

user_login = Blueprint('user_login', __name__, url_prefix='/user/login')


# 普通用户登录
@user_login.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('user_admin.index'))
    return render_template('user/login/index.html')


# 登录
@user_login.post('/')
def login_post():
    req = request.form
    print(req)
    email = req.get('email')
    if not re.match(r'^[0-9a-za-z_]{0,19}@[0-9a-za-z]{1,13}\.[com,cn,net]{1,3}$', email):
        return fail_api(msg="请输入正确的邮箱账号!")
    password = req.get('password')
    code = req.get('captcha').__str__().lower()

    if not email or not password or not code:
        return fail_api(msg="请输入用户名或密码!")
    s_code = session.get("code", None)
    session["code"] = None

    if not all([code, s_code]):
        return fail_api(msg="参数错误")

    if code != s_code:
        return fail_api(msg="验证码错误")
    user = User.query.filter_by(email=email).first()

    if not user:
        return fail_api(msg="不存在的用户,请先注册账号")

    if user.enable == 0:
        return fail_api(msg="该用户已经被封禁!")

    if email == user.email and user.validate_password(password):
        # 登录
        login_user(user)
        # 记录登录日志
        login_log(request, uid=user.id, is_access=True)
        # 存入权限
        index_curd.add_auth_session()
        return success_api(msg="登录成功")
    login_log(request, uid=user.id, is_access=False)
    return fail_api(msg="邮箱或密码错误")
