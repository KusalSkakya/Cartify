from flask import Flask, redirect
from config import Config
from API.database.database import init_app
from API.controllers.product_controller import product_controller


app = Flask(__name__)
app.config.from_object(Config)

init_app(app)

app.register_blueprint(product_controller)

@app.route('/')
def home():
    return redirect('/main')
if __name__ == "__main__":
    app.run(debug=True)



# from flask import Flask, render_template
# from flask_mysqldb import MySQL
# from config import Config
# from database.database import init_app, mysql
# from API.controllers.product_controller import product_controller

# app = Flask(__name__)
# app.config.from_object(Config)

# app.register_blueprint(product_controller)


# init_app(app)


# mysql = MySQL(app)


# def init_app(app):
#     mysql.init_app(app)
#     return mysql




# if __name__ == '__main__':
#     app.run(debug=True)


# class config:
#     MYSQL_HOST = 'localhost'
#     MYSQL_USER = 'root'
#     MYSQL_PASSWORD = 'abcd1234'
#     MYSQL_DB = 'cartify'



# # app = Flask(__name__)
# # app.config['MYSQL_HOST'] = 'localhost'
# # app.config['MYSQL_USER'] = 'root'
# # app.config['MYSQL_PASSWORD'] = 'abcd1234'
# # app.config['MYSQL_DB'] = 'cartify'

# @app.route('/')
# def data():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM products")
#     products = cur.fetchall()
#     cur.close()
#     return render_template('Homepage.HTML', products=products)


# @app.route('/')
# def abtdata():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM products")
#     products = cur.fetchall()
#     cur.close()
#     return render_template('about.html', products=products)



# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/Signin')
# def signin():
#     return render_template('signin.html')


# @app.route('/about')
# def about():
#     return render_template('about.html')


# @app.route('/cart')
# def cart():
#     return render_template('cart.html')


