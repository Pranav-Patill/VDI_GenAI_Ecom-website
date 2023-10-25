from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json

views = Blueprint('views', __name__)

products = [
  {'name': 'Product 1', 'image': 'product1.jpg', 'description': 'Description 1','price':100},
  {'name': 'Product 2', 'image': 'product2.jpg', 'description': 'Description 2','price':150},
  {'name': 'Product 3', 'image': 'product3.jpg', 'description': 'Description 3','price':45},
  {'name': 'Product 4', 'image': 'product4.jpg', 'description': 'Description 4','price':600},
  {'name': 'Product 5', 'image': 'product5.jpg', 'description': 'Description 5','price':400},
  {'name': 'Product 6', 'image': 'product6.jpg', 'description': 'Description 6','price':220},
  {'name': 'Product 7', 'image': 'product7.jpg', 'description': 'Description 7','price':10}
]

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user, items=products)

@views.route('/cart', methods=['GET', 'POST'])
@login_required
def cart():
    return render_template("cart.html", user=current_user)
