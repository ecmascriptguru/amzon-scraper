from flask import Blueprint

spiders = Blueprint('spiders', __name__)

from selenium_browser import UBrowse