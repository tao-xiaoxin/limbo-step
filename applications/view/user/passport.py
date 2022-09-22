from flask import Blueprint
from applications.common.utils.mail import send_mail
from applications.extensions.init_redis import *
user_passport = Blueprint('user_passport', __name__, url_prefix='/user/passport')


@user_passport.route('/')
def index():

    return "这是user/passport路由"

# 发送邮箱验证码
@user_passport.route('/code')
def passport_post():
    return "这是user/passport路由"
