import os
from sqlalchemy import create_engine

import urllib
class Config(object):
    SECRET_KEY='MY_SECRET_KEY'
    SESSION_COKIE_SECURE=False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://pau:123456@127.0.0.1:3308/idgs804'