
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask._app_ctx_stack import _app_ctx_stack
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from werkzeug.security import generate_password_hash
from models import db, Customer, Merchant
from signup import register_customer, register_merchant
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # Use your database URI
db.init_app(app)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/customer', methods=['GET', 'POST'])
def register_customer_route():
    return register_customer()

@app.route('/register/merchant', methods=['GET', 'POST'])
def register_merchant_route():
    return register_merchant()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables based on models
    app.run(debug=True)
