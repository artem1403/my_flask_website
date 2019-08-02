from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    openid = TextField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)