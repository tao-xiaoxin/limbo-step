#!/bin/sh
exec gunicorn -c gunicorn.conf.py "applications:create_app('development')"
nohup python3 task.py >logs/crontab.log 2>&1 &