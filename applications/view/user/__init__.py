from flask import Flask
from applications.view.user.login import user_login
from applications.view.user.admin import user_admin
from applications.view.user.register import user_register
from applications.view.user.passport import user_passport
from applications.view.user.configs import user_configs


def register_user_views(app: Flask):
    app.register_blueprint(user_admin)
    app.register_blueprint(user_register)
    app.register_blueprint(user_passport)
    app.register_blueprint(user_configs)
    app.register_blueprint(user_login)