"""
Base class of spiders
"""

from flask import Blueprint
from category import CategorySpider

spiders = Blueprint('spiders', __name__)

class Spider(object):
    """
    docstring for Spider
    """
    def __init__(self):
        pass
    
    def run(self):
        spider = CategorySpider()
        spider.run()