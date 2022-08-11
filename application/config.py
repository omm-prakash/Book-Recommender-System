import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = True

class LocalDevelopmentConfig(Config):
    DEBUG = True

