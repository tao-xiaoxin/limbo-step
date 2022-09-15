from flask import Blueprint

user_admin = Blueprint('user_admin', __name__, url_prefix='/user/admin')


@user_admin.route('/')
def index():
    return "这是user/admin路由"