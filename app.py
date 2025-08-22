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

