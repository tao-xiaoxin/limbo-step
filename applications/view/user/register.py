from flask import Blueprint
from applications import models

user_register = Blueprint('user_register', __name__, url_prefix='/user/register')


@user_register.route('/')
def index():
    return "这是user/register路由"
