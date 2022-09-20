# flask配置
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=1
FLASK_RUN_HOST = 127.0.0.1
FLASK_RUN_PORT = 5000

# pear admin flask配置
SYSTEM_NAME = Limbo Microstep

# MySql配置信息
MYSQL_HOST=127.0.0.1
# MYSQL_HOST=dbserver
MYSQL_PORT=3306
MYSQL_DATABASE=PearAdminFlask
MYSQL_USERNAME=root
MYSQL_PASSWORD=123456

# Redis 配置
REDIS_HOST=127.0.0.1
REDIS_PORT=6379
REDIS_PASSWORD=123456

# 百度内容审核配置
BAIDU_POWER=False   # 内容审核是否开启
BAIDU_API_KEY=''    # 百度应用APPID
BAIDU_API_KEY=''    # 百度应用SECRETKEY

# 密钥配置(记得改)
SECRET_KEY='pear-admin-flask'

# 邮箱配置
MAIL_SERVER='smtp.qq.com'
MAIL_USERNAME='123@qq.com'
MAIL_PASSWORD='XXXXX' # 生成的授权码