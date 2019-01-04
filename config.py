import logging
import redis
import os


class Config(object):
    BASE_DIR = os.path.dirname(__file__)
    # sql数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@localhost/test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # Session相关配置
    # redis数据库地址
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    # 存储的数据库
    SESSION_TYPE = "redis"
    # 密钥
    SECRET_KEY = "vXform207w2Flq8iLFpksE1WwfCDOqFDgNV4VL4hpnCIXTTg3Z5+QlJObtk4X9Sj9DngkbC05KXe7bJxqrihw=="
    # 用户签名
    SESSION_USE_SIGNER = True
    # 保存时间
    PERMANENT_SESSION_LIFETIME = 86400 * 7
    # 数据库地址
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)


class DevelopmentConfig(Config):
    # 开发模式
    DEBUG = True
    LOG_LEVEL = logging.DEBUG


class ProductionConfig(Config):
    # 生产模式
    DEBUG = False
    LOG_LEVEL = logging.WARNING
