#!/bin/sh
exec gunicorn -c gunicorn.conf.py "applications:create_app('development')"