from flask import Blueprint, session, redirect, url_for, render_template, request
from flask_login import current_user, login_user, login_required, logout_user

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
    return render_template('user/login/login.html')
