import logging
import os


class BaseConfig:
    SYSTEM_NAME = os.getenv('SYSTEM_NAME', 'Limbo Microstep')
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 主题面板的链接列表配置
    SYSTEM_PANEL_LINKS = [
        {
            "icon": "layui-icon layui-icon-auz",
            "title": "开源地址",
            "href": "https://github.com/tao-xiaoxin/limbo-step"
        }
    ]

    UPLOADED_PHOTOS_DEST = 'static/upload'
    UPLOADED_FILES_ALLOW = ['gif', 'jpg']

    # JSON配置
    JSON_AS_ASCII = False

    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    # 默认日志等级
    LOG_LEVEL = logging.WARN
    # 推送加token
    PLUS_TOKEN = os.getenv("PLUS_TOKEN") or ''
    # 日志文件
    LOG_FILE = os.getenv("LOG_FILE") or 'limbo.log'


class DevelopmentConfig(BaseConfig):
    """ 开发配置 """
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False


class ProductionConfig(BaseConfig):
    """生成环境配置"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    LOG_LEVEL = logging.ERROR


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

configs = BaseConfig()
