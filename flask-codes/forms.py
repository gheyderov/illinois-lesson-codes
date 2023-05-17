from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    company = StringField('company')
    message = TextAreaField('message')
    is_subscribe = BooleanField()


class RegisterForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = StringField('name', validators=[DataRequired()])
    confirm_password = StringField('name', validators=[DataRequired(), EqualTo('password')])


class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = StringField('name', validators=[DataRequired()])

