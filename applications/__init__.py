import os
from flask import Flask

from applications.common.script import init_script
from applications.extensions import init_plugs
from applications.view import init_view
from applications.configs import config


def create_app(config_name=None):
    app = Flask(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

    if not config_name:
        # 尝试从本地环境中读取
        config_name = os.getenv('FLASK_CONFIG', 'development')

    # 引入数据库配置
    app.config.from_object(config[config_name])

    # 注册各种插件
    init_plugs(app)

    # 注册路由
    init_view(app)

    # 注册命令
    init_script(app)

    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        logo()

    return app


def logo():
    print('''
         へ　　　　　／|
    　　/＼7　　　 ∠＿/
    　 /　│　　 ／　／
    　│　Z ＿,＜　／　　 /`ヽ
    　│　　　　　ヽ　　 /　　〉
    　 Y　　　　　`　 /　　/
    　ｲ●　､　●　　⊂⊃〈　　/
    　()　 へ　　　　|　＼〈
    　　>ｰ ､_　 ィ　 │ ／／
    　 / へ　　 /　ﾉ＜| ＼＼
    　 ヽ_ﾉ　　(_／　 │／／
    　　7　　　　　　　|／
    　　＞―r￣￣`ｰ―＿
        ''')
