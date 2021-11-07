from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField
from wtforms.fields.core import BooleanField
from wtforms.fields.simple import PasswordField, SubmitField, TextAreaField
from wtforms.validators import *

from flask_login import current_user
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(
        min=2, max=20)], render_kw={'autofocus': True})

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=8)])

    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign up')

    # to prevent the same username being used twice
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is already taken. Please use another one')

    # to prevent the same email being used twice
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'That username is already taken. Please choose another one')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
                        DataRequired(), Email()], render_kw={'autofocus': True})
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)], render_kw={'autofocus': True})

    email = StringField('Email', validators=[DataRequired(), Email()])

    picture = FileField('Update profile picture', validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Update')

    # to prevent the same username being used twice
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'That email is already taken. Please use another one')

    # to prevent the same email being used twice
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    'That username is already taken. Please choose another one')


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                'There is no account with that email. Please use another one')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
