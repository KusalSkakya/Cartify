from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from API.repositorys.product_repository import get_all_products
from API.database.database import mysql
from werkzeug.security import generate_password_hash, check_password_hash

product_controller = Blueprint("product_controller", __name__)

@product_controller.route('/main')
def Main():
    products = get_all_products()
    return render_template('homepage.html', products=products)

@product_controller.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cur = mysql.connection.cursor()
        cur.execute("SELECT id, user_password FROM users WHERE user_name = %s", (username,))
        user = cur.fetchone()
        cur.close()

        if user and check_password_hash(user[1], password):
            session["user_id"] = user[0]
            flash("Login successful!", "success")
            return redirect(url_for("product_controller.Main"))
        else:
            flash("Invalid username or password", "danger")
            return redirect(url_for("product_controller.login"))

    return render_template('login.html')

@product_controller.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            flash("Passwords do not match!", "danger")
            return redirect(url_for("product_controller.signin"))

        hashed_password = generate_password_hash(password)

        cur = mysql.connection.cursor()
        try:
            cur.execute(
                "INSERT INTO users (user_name, user_password, email) VALUES (%s, %s, %s)",
                (username, hashed_password, email)
            )
            mysql.connection.commit()
            cur.close()
            flash("Account created successfully! Please log in.", "success")
            return redirect(url_for("product_controller.login"))
        except Exception as err:
            flash(f"Error: {err}", "danger")
            return redirect(url_for("product_controller.signin"))

    return render_template('signin.html')

@product_controller.route('/about')
def about():
    products = get_all_products()
    return render_template('about.html', products=products)

@product_controller.route('/cart')
def cart():
    return render_template('cart.html')




