from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from passlib.hash import pbkdf2_sha256
from models import User

#custom validation
#username and password checker
def invalid_credentials(form, field):
    username_entered  = form.username.data
    password_entered = field.data

    #check if creds are valid
    user_object = User.query.filter_by(username=username_entered).first()
    if user_object is None:
        raise ValidationError("Username or password is incorrect.")
    elif not pbkdf2_sha256.verify(password_entered, user_object.password):
        raise ValidationError("Username or password is incorrect.")




class RegistrationForm(FlaskForm):
    username = StringField('username_label', validators=[InputRequired(message="Username required"), Length(min=4, max=25, message="Username must be between 4 and 25 characters")])
    password = PasswordField('password_label', validators=[InputRequired(message="Password required"), Length(min=4, max=25, message="Password must be between 4 and 25 characters")])
    confirm_password = PasswordField('confirm_password_label', validators=[InputRequired(message="Password required"), EqualTo('password', message="Passwords must match")])
    submit_button = SubmitField('Create')


    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username already exists. Choose another!!")


class LoginForm(FlaskForm):
    username = StringField('username_label', validators=[InputRequired(message="Username required")])
    password = PasswordField('password_label', validators=[InputRequired(message="Password required"), invalid_credentials])
    submit_button = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('username_label', validators=[InputRequired(message="username required")])
    firstname = StringField('firstname_label', validators=[InputRequired(message="firstname required")])
    lastname = StringField('lastname_label', validators=[InputRequired(message="lastname required")])
    address = StringField('address_label', validators=[InputRequired(message="address required")])
    mobileno = StringField('mobileno_label', validators=[InputRequired(message="mobileno required")])
    #email = StringField('Email',validators=[DataRequired(), Email()])
    #picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit_update = SubmitField('Update')


class CheckOutForm(FlaskForm):
    Full_Name = StringField('Full_Name_label', validators=[InputRequired(message="Full Name")])
    Email = StringField('Email_label', validators=[InputRequired(message="name@gmail.com")])
    Address = StringField('Address _label', validators=[InputRequired(message="Flat No, Building Name, Street Name")])
    City = StringField('City_label', validators=[InputRequired(message="City")])
    State = StringField('State_label', validators=[InputRequired(message="State")])
    Pin_Code = StringField('Pin_Code_label', validators=[InputRequired(message="Pin Code")])
    Name_on_Card = StringField('Name_on_Card_label', validators=[InputRequired(message="Name")])
    Credit_card_number = StringField('Credit_card_number_label', validators=[InputRequired(message="1111-2222-3333-4444")])
    Exp_Month = StringField('Exp_Month_label', validators=[InputRequired(message="Month")])
    Exp_Year = StringField('Exp_Year_label', validators=[InputRequired(message="Year")])
    CVV = StringField('CVV_label', validators=[InputRequired(message="000")])
    #email = StringField('Email',validators=[DataRequired(), Email()])
    #picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit_checkout = SubmitField('CheckOut')



#    def validate_email(self, email):
#        if email.data != current_user.email:
#            user = User.query.filter_by(email=email.data).first()
#            if user:
#                raise ValidationError('That email is taken. Please choose a different one.')
