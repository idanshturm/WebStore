"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, Regexp




class SignupForm(FlaskForm):
    """User Sign-up Form."""
    name = StringField(
        'username',
        validators=[
          DataRequired(),    
          Regexp('^\w+$', message="Username must contain only letters numbers or underscore")
          
        ]       
             
    )
    
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, message='Select a stronger password.')
        ]
    )
    
    confirm = PasswordField(
        'Confirm Your Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
  
    submit = SubmitField('Register')
    

class LoginForm(FlaskForm):
    name = StringField(
        'username',
        validators=[DataRequired(),
        Regexp('^\w+$', message="Username must contain only letters or numbers")
          

        ]       
             
    )          
             
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class SearchForm(FlaskForm):    
    name = StringField(
        'Search_Product',
        validators=[
            DataRequired(),
            Regexp('^[a-zA-Z\x20]+$', message="Username must contain only letters")  
        ]
    )
    submit = SubmitField('Search')


class InsertForm(FlaskForm):
    name = StringField(
        'Name of The Product',
        validators=[
            DataRequired(),
            Regexp('^[a-zA-Z\x20]+$', message="Username must contain only letters")
            
        ]
        
    )
    
    price = StringField(
        'enter your price',
        validators=[
            DataRequired(),
            Length(max=10, message='too many numbers.'),
            Regexp('^[0-9]*$', message="Username must contain only l numbers or")
            
        ]
    )
    
    amount = StringField(
        'enter your amount',
        validators=[
            DataRequired(),
            Length(max=1000, message='too many numbers'),
            Regexp('^[0-9]*$', message="Username must contain only  numbers or ")
            
        ]
    )
  
    submit = SubmitField('Insert')
