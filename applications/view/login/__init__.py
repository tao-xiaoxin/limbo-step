from flask import Flask
from applications.view.login.index import login_index


def register_login_views(app: Flask):
    app.register_blueprint(login_index)