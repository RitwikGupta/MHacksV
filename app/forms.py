from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired  #not sure if we need a form?

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()]) #data-text.csv
    remember_me = BooleanField('remember_me', default=False)
