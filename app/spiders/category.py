"""
docsting for category class
"""

from selenium_browser import UBrowse
from ..models import *

class CategorySpider(object):
    """
    Category spider for amazon products.
    """
    def __init__(self, domain = "amazon.com"):
        self.domain = Domain.query.filter_by(name=domain).first()
        self.client = None

    def run(self):
        print("""
        Starting Category Scraper....
        """)
        if self.client is None:
            self.client = UBrowse()
        


if __name__ == "__main__":
    spider = CategorySpider()
    spider.run()