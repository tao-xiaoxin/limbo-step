from applications.views.view import index_bp
from .view import index


def register_index_views(app):
    """
    初始化蓝图

    """
    app.register_blueprint(index_bp)


def init_view(app):
    register_index_views(app)
