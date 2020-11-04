from flask import Flask, render_template, redirect, url_for
from passlib.hash import pbkdf2_sha256 #password based key dervation func version2 for hashing
from flask_login import LoginManager,login_user, current_user, login_required, logout_user
from wtform_fields import *
from models import *

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



#always true
if __name__ == "__main__":
    app.run(debug=True)