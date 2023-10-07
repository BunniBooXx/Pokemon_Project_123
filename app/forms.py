from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class SearchForm(FlaskForm):
    query= StringField(label='Search',validators=[DataRequired()])
    submit= SubmitField(label='Submit')

class SignUpForm(FlaskForm): 
    Username= StringField(label='Username',validators=[DataRequired()])
    Email=StringField(label='Email', validators=[DataRequired()])
    Password=StringField(label='Password', validators=[DataRequired()])
    Confirm_Password=StringField(label='Confirm Password', validators=[DataRequired(), EqualTo('Password')])
    submit=SubmitField(label='Sign Up')


class Login(FlaskForm):
    Username=StringField(label='Username', validators=[DataRequired()])
    Password= StringField(label='Password', validators=[DataRequired()])
    submit=SubmitField(label='Login')