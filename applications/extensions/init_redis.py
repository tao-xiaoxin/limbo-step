from flask import Flask as app
from flask_caching import Cache
from applications.configs.config import configs
cache = Cache()


def redis(app=app,redis_db=0,cache_type=configs.CACHE_TYPE):
    cache.init_app(app,config={{
        'CACHE_TYPE' :cache_type,
        'CACHE_REDIS_HOST':configs.REDIS_HOST,
        'CACHE_REDIS_PORT':configs.REDIS_PORT,
        "CACHE_REDIS_PASSWORD":configs.REDIS_PASSWORD,
        "CACHE_REDIS_DB":redis_db,
    }})
    return cache