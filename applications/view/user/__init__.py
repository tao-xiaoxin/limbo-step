from flask import Flask
from applications.view.user.register import user_register


def register_user_views(app: Flask):
    app.register_blueprint(user_register)