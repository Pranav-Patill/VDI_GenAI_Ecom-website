from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, session
from flask_login import login_required, current_user
from . import db
import json


views = Blueprint('views', __name__)



@views.route('/',methods=['GET', 'POST'])
def index():
  if current_user.is_authenticated:
    return redirect(url_for('views.home'))
  else:
    return redirect(url_for('auth.login'))

@views.route('/home',methods=['GET', 'POST']) 
@login_required
def home():
  products = [
  {'name': 'Product 1', 'image': 'product1.jpg', 'description': 'Description 1','product_id':'p1','price':100},
  {'name': 'Product 2', 'image': 'product2.jpg', 'description': 'Description 2','product_id':'p2','price':150},
  {'name': 'Product 3', 'image': 'product3.jpg', 'description': 'Description 3','product_id':'p3','price':45},
  {'name': 'Product 4', 'image': 'product4.jpg', 'description': 'Description 4','product_id':'p4','price':600},
  {'name': 'Product 5', 'image': 'product5.jpg', 'description': 'Description 5','product_id':'p5','price':400},
  {'name': 'Product 6', 'image': 'product6.jpg', 'description': 'Description 6','product_id':'p6','price':220},
  {'name': 'Product 7', 'image': 'product7.jpg', 'description': 'Description 7','product_id':'p7','price':10}
  ]
  return render_template("home.html", user=current_user, items=products)

@views.route('/cart', methods=['GET', 'POST'])
@login_required
def cart():
  cart_items = [
  {'name': 'Product 1', 'image': 'product1.jpg', 'description': 'Description 1','product_id':'p1','price':100,'quantity':4},
  {'name': 'Product 2', 'image': 'product2.jpg', 'description': 'Description 2','product_id':'p2','price':150,'quantity':2},
  {'name': 'Product 3', 'image': 'product3.jpg', 'description': 'Description 3','product_id':'p3','price':45,'quantity':7}
  ]
  
  total = sum(item['price'] * item['quantity'] for item in cart_items)
  
  return render_template("cart.html", user=current_user, cart_items=cart_items, cart_total=total)

@views.route('/add_to_cart', methods=['POST'])
def add_to_cart():
  product_id = request.form['product_id']
  from .models import Cart
  # Get current user's cart
  cart = Cart.query.filter_by(user_id=current_user.id).first()

  # Commit to database
  db.session.commit()
  
  return jsonify({'success': True})

