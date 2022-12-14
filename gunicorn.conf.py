import os
import multiprocessing

bind = '0.0.0.0:9000'
backlog = 512
chdir = os.path.dirname(os.path.abspath(__file__))
timeout = 30
worker_class = 'gevent'  # 使用gevent模式，还可以使用sync 模式，默认的是sync模式

workers=2
threads = 2
loglevel = 'info'
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'

if not os.path.exists('logs'):
    os.mkdir('logs')

accesslog = os.path.join(chdir, "logs/gunicorn_access.log")
errorlog = os.path.join(chdir, "logs/gunicorn_error.log")

# 代码发生变化是否自动重启
reload=True
