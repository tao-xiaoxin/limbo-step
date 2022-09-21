from flask_login import current_user, login_user, login_required, logout_user
from applications.common import admin as index_curd
from applications.common.admin_log import login_log
from flask import Blueprint, session, redirect, url_for, render_template, request

user_admin = Blueprint('user_admin', __name__, url_prefix='/user/admin')


@user_admin.route('/')
def index():
    # 当前用户
    if current_user.is_authenticated:
        user = current_user
        return render_template('user/admin/index.html', user=user)
    return render_template('user/login/index.html')
