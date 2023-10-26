from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id= db.Column(db.String(5))
    name = db.Column(db.String(150))
    price = db.Column(db.Float)
    image = db.Column(db.String(150))
    description = db.Column(db.String(150))
    cart_item = db.relationship('Cart')

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_item = db.Column(db.String, db.ForeignKey('product.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #foreign key stored in child 

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    cart_item = db.relationship('Cart') #parent