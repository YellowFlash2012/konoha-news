from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed 
from wtforms import StringField
from wtforms.fields.core import BooleanField
from wtforms.fields.simple import PasswordField, SubmitField, TextAreaField
from wtforms.validators import *
from wtforms.widgets.core import TextArea

from flaskblog.models import User
from flask_login import current_user




