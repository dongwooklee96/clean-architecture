import os

basedir = os.path.abspath(os.ath.dirname(__file__))


class Config(object):
    """Base Configuration"""


class ProductionConfig(Config):
    """Production Configuration"""


class DevelopmentConfig(Config):
    """Development Configuration"""


class TestingConfig(Config):
    """Testing configutation"""

    TESTING = True