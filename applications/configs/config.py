import logging
import os
from urllib.parse import quote_plus as urlquote


class BaseConfig:
    SYSTEM_NAME = os.getenv('SYSTEM_NAME', 'Limbo Microstep')
    # 主题面板的链接列表配置
    SYSTEM_PANEL_LINKS = [
        # {
        #     "icon": "layui-icon layui-icon-auz",
        #     "title": "官方网站",
        #     "href": "http://www.pearadmin.com"
        # },
        {
            "icon": "layui-icon layui-icon-auz",
            "title": "开发文档",
            "href": "http://www.pearadmin.com"
        },
        {
            "icon": "layui-icon layui-icon-auz",
            "title": "开源地址",
            "href": "https://gitee.com/Jmysy/Pear-Admin-Layui"
        }
    ]

    UPLOADED_PHOTOS_DEST = 'static/upload'
    UPLOADED_FILES_ALLOW = ['gif', 'jpg']

    # JSON配置
    JSON_AS_ASCII = False

    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    # redis配置
    REDIS_HOST = os.getenv('REDIS_HOST') or "127.0.0.1"
    REDIS_PORT = int(os.getenv('REDIS_PORT') or 6379)
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD") or "123456"

    # Redis 配置信息
    REDIS_URL = f'redis://:{REDIS_PASSWORD or ""}@{REDIS_HOST}:6380'

    # mysql 配置
    MYSQL_USERNAME = os.getenv('MYSQL_USERNAME') or "root"
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD') or "123456"
    MYSQL_HOST = os.getenv('MYSQL_HOST') or "127.0.0.1"
    MYSQL_PORT = int(os.getenv('MYSQL_PORT') or 3306)
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE') or "PearAdminFlask"

    # mysql 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{urlquote(MYSQL_PASSWORD)}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"

    # 默认日志等级
    LOG_LEVEL = logging.WARN

    # 邮箱配置
    MAIL_SERVER = os.getenv('MAIL_SERVER') or 'smtp.qq.com'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    MAIL_USERNAME = os.getenv('MAIL_USERNAME') or '123@qq.com'
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD') or 'XXXXX'  # 生成的授权码
    # 默认发件人的邮箱,这里填写和MAIL_USERNAME一致即可
    MAIL_DEFAULT_SENDER = ('Limbo Microstep', os.getenv('MAIL_USERNAME') or '123@qq.com')

    # 百度内容审核配置
    BAIDU_POWER = os.getenv("BAIDU_POWER") or False  # 内容审核是否开启
    BAIDU_API_KEY = os.getenv("BAIDU_API_KEY") or ""  # 百度应用APPID
    BAIDU_SECRET_KEY = os.getenv("BAIDU_API_KEY") or ''  # 百度应用SecretKey


class TestingConfig(BaseConfig):
    """ 测试配置 """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # 内存数据库


class DevelopmentConfig(BaseConfig):
    """ 开发配置 """
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False


class ProductionConfig(BaseConfig):
    """生成环境配置"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_RECYCLE = 8

    LOG_LEVEL = logging.ERROR


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
