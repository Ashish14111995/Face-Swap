class Config(object):

    SECRET_KEY = 'Ashish'

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

class DevelopmentConfig(Config):
    DEBUG = True
