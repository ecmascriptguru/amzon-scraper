"""
Basic Configurations
"""

class Config(object):
    """
    docstring for Config
    """
    def __init__(self):
        pass


class DevelomentConfig(Config):
    """
    Dev Config
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'dskfjlskdj34985&d8&^'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/amazon'
    CHROME_DRIVER_PATH = 'F:/workspace/chrome/chromedriver.exe'


class StagingConfig(Config):
    """
    Staging Config
    """
    DEBUG = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class ProductionConfig(Config):
    """
    Production Config
    """
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app_config = {
    'dev': DevelomentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}
