"""
docstring for models
"""

from . import db

class Domain(db.Model):
    """
    Domains Table
    """
    __tablename__ = "domains"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    categories = db.relationship("Category", backref="categories", lazy="dynamic")

    def __repr__(self):
        return '<Domain: {}>'.format(self.name)

class Category(db.Model):
    """
    Categories Table
    """
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    domain_id = db.Column(db.Integer, db.ForeignKey("domains.id"), default=None)
    parent_id = db.Column(db.Integer, default=None)
    name = db.Column(db.String(50))
    url = db.Column(db.UnicodeText)
    domain = db.relationship(Domain)
    products = db.relationship("Product", backref="products", lazy="dynamic")

    def __repr__(self):
        return '<Category: {0} at {1}>'.format(self.name, self.domain.name)

class Product(db.Model):
    """
    Products Table
    """
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    domain_id = db.Column(db.Integer, db.ForeignKey("domains.id"), default=None)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), default=None)
    asin = db.Column(db.String(20))
    domain = db.relationship(Domain)
    category = db.relationship(Category)

    def __repr__(self):
        return '<Product: {0} at {1}>'.format(self.asin, self.domain.name)
