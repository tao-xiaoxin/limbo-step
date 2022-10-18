from flask import Flask
from applications.view.push.plus import push_plus


def register_push_views(app: Flask):
    app.register_blueprint(push_plus)