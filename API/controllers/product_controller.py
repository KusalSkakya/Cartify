from flask import Blueprint, render_template
from API.repositorys.product_repository import get_all_products

product_controller= Blueprint("product_controller", __name__)

@product_controller.route('/main')
def Main():
    products = get_all_products()
    return render_template('homepage.html', products=products)

@product_controller.route('/login')
def login():
    return render_template('login.html')

@product_controller.route('/Signin')
def signin():
    return render_template('signin.html')

@product_controller.route('/about')
def about():
    return render_template('about.html')

@product_controller.route('/cart')
def cart():
    return render_template('cart.html')