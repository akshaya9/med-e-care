from flask import Flask, render_template, redirect, url_for,flash
from passlib.hash import pbkdf2_sha256 #password based key dervation func version2 for hashing
from flask_login import LoginManager,login_user, current_user, login_required, logout_user
from wtform_fields import *
from models import *
from flask import session
from sqlalchemy.orm.exc import UnmappedClassError, UnmappedInstanceError


app  = Flask(__name__)
app.secret_key = 'should be changed'

app.config['SQLALCHEMY_DATABASE_URI']='postgres://gkuebhlmxhtjau:5e496cb9299ee89363d408be21367dab4dd1745fb45bed374f8a787bad39fd7c@ec2-52-2-82-109.compute-1.amazonaws.com:5432/d349hchhak43qj'
db = SQLAlchemy(app)

#Configure flask login
login = LoginManager(app)
login.init_app(app)

@login.user_loader(id)
def load_user(id):
    return User.query.get(int(id))

@app.route("/", methods=['GET', 'POST'])
def index():
    reg_form = RegistrationForm()
    # updates db if validation is successfull
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password  =reg_form.password.data

        #hash password
        hashed_pswd = pbkdf2_sha256.hash(password)
        #adding user to db
        user = User(username=username, password=hashed_pswd)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template("index.html", form=reg_form)


@app.route("/login",methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    #allows login if validation is sucessfull
    if login_form.validate_on_submit():
        user_object = User.query.filter_by(username=login_form.username.data).first()
        login_user(user_object)
        return redirect(url_for('dashboard'))

    return render_template("login.html", form=login_form)

@app.route("/dashboard", methods=['GET', 'POST'])
# @login_required
def dashboard():
    # if not current_user.is_authenticated:
    #     return current_app.login_manager.unauthorized()
    return "Welcome to dashboard!"


@app.route("/logout", methods=['GET'])
def logout():
    logout_user()
    return "You've logged out successfully!"


@app.route('/account',methods = ['POST', 'GET'])
def account():
    UpdateAccount_form = UpdateAccountForm()
    if UpdateAccount_form.validate_on_submit():
        #import pdb; pdb.set_trace()
        username = UpdateAccount_form.username.data
        firstname= UpdateAccount_form.firstname.data
        lastname= UpdateAccount_form.lastname.data
        address= UpdateAccount_form.address.data
        mobileno= UpdateAccount_form.mobileno.data
        old_user =UpdateUser.query.filter_by(username=username).first()
        if bool(old_user):
            old_user.firstname= firstname
            old_user.lastname= lastname
            old_user.address= address
            old_user.mobileno= mobileno
            db.session.merge(old_user)
            db.session.commit()
            flash("Details Updated successfully")
            return render_template("account.html", form= UpdateAccount_form)
        new_user = UpdateUser( username=username,firstname=firstname, lastname=lastname, address=address, mobileno=mobileno)
        db.session.add(new_user)
        db.session.commit()
        flash("Details saved successfully")
        return render_template("account.html", form= UpdateAccount_form)
    return render_template("account.html",form= UpdateAccount_form)

@app.route("/checkout", methods=['GET', 'POST'])
# @login_required
def checkout():
    checkout_form = CheckOutForm()
    if checkout_form.validate_on_submit():
        #import pdb; pdb.set_trace()
        Full_Name = checkout_form.Full_Name.data
        Email = checkout_form.Email.data
        Address = checkout_form.Address.data
        City = checkout_form.City.data
        State = checkout_form.State.data
        Pin_Code = checkout_form.Pin_Code.data
        Name_on_Card = checkout_form.Name_on_Card.data
        Credit_card_number = checkout_form.Credit_card_number.data
        Exp_Month = checkout_form.Exp_Month.data
        Exp_Year = checkout_form.Exp_Year.data
        CVV = checkout_form.CVV.data
        #new_user = UpdateUser( username=username,firstname=firstname, lastname=lastname, address=address, mobileno=mobileno)
        #db.session.add(new_user)
        #db.session.commit()
        flash("Order Placed Successfully")
        return render_template("checkout.html",form= checkout_form)
    return render_template("checkout.html",form= checkout_form)


#always true
if __name__ == "__main__":
    app.run(debug=True)
