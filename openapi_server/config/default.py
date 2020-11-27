import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'historic_super_secret_key'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://eajqjsmpybzzsb:57299d6e97a50490ba632dcb9349ab709596083ea5854f82d44004712bec49c6@ec2-54-217-236-206.eu-west-1.compute.amazonaws.com:5432/d8ca6n547ht0fo'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost"


class TestingConfig(Config):
    TESTING = True