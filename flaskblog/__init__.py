from flask import Flask
import os

from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '31a1a8c2a033332e089e4432471d15ce'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #login here is the name of login() in routes
login_manager.login_message_category = 'info' #info is a bootsrap category

# config for sending emails
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)


from flaskblog import routes