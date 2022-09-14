from flask import Blueprint

login_index = Blueprint('login_index', __name__, url_prefix='/login/index')


@login_index.route('/')
def index():
    return "这是login/index路由"