from flask_wtf import FlaskForm
from wtforms import StringField

from wtforms.fields.simple import PasswordField, SubmitField, TextAreaField
from wtforms.validators import *

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
