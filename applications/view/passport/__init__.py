from flask import Blueprint, session, redirect, url_for, render_template, request
from flask_login import current_user, login_user, login_required, logout_user
from applications.common.utils import send_mail
from applications.common import admin as index_curd
from applications.common.admin_log import login_log
from applications.common.utils.http import fail_api, success_api
from applications.models import User
import re
passport_bp = Blueprint('passport', __name__, url_prefix='/passport')


def register_passport_views(app):
    app.register_blueprint(passport_bp)


# 获取验证码
@passport_bp.get('/getCaptcha')
def get_captcha():
    resp, code = index_curd.get_captcha()
    session["code"] = code
    return resp




# 登录
@passport_bp.get('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))
    return render_template('admin/login.html')


# 登录
@passport_bp.post('/login')
def login_post():
    req = request.form
    email = req.get('email')
    password = req.get('password')
    code = req.get('captcha').__str__().lower()

    if not email or not password or not code or not re.match(
            r'^[0-9a-za-z_]{0,19}@[0-9a-za-z]{1,13}\.[com,cn,net]{1,3}$', email):
        return fail_api(msg="请输入正确的邮箱账号或密码!")
    s_code = session.get("code", None)
    session["code"] = None

    if not all([code, s_code]):
        return fail_api(msg="参数错误")

    if code != s_code:
        return fail_api(msg="验证码错误")
    user = User.query.filter_by(email=email).first()

    if not user:
        return fail_api(msg="不存在的用户")

    if user.enable == 0:
        return fail_api(msg="用户被暂停使用")

    if email == user.email and user.validate_password(password):
        # 登录
        login_user(user)
        # 记录登录日志
        login_log(request, uid=user.id, is_access=True)
        # 存入权限
        index_curd.add_auth_session()
        return success_api(msg="登录成功")
    login_log(request, uid=user.id, is_access=False)
    return fail_api(msg="用户名或密码错误")


# 退出登录
@passport_bp.post('/logout')
@login_required
def logout():
    logout_user()
    session.pop('permissions')
    return success_api(msg="注销成功")
