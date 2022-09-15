from flask import Flask
from applications.view.user.login import user_login
from applications.view.user.admin import user_admin
from applications.view.user.register import user_register


def register_user_views(app: Flask):
    app.register_blueprint(user_admin)
    app.register_blueprint(user_register)
    app.register_blueprint(user_login)