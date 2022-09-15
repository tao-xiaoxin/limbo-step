from flask import Blueprint

user_register = Blueprint('user_register', __name__, url_prefix='/user/register')


@user_register.route('/')
def index():
    return "这是user/register路由"