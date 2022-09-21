from flask import Blueprint
from ...common import admin
from flask_login import login_required

user_configs = Blueprint('user_configs', __name__, url_prefix='/user/configs')


# 普通用户配置
@user_configs.route('/')
@login_required
def configs():
    return admin.get_user_config()
