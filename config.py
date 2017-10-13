class Config(object):
    """
    Configurations
    """


class DevelomentConfig(Config):
    """
    Dev Config
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'dskfjlskdj34985&d8&^'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/amazon'
    CHROME_DRIVER_PATH = 'F:/workspace/Alex Richard/Afaq Khan/amzon-scraper/app/spiders/chrome/chromedriver.exe'


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