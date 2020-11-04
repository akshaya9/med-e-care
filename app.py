from flask import Flask, render_template, redirect, url_for
from passlib.hash import pbkdf2_sha256 #password based key dervation func version2 for hashing
from wtform_fields import *
from models import *

app  = Flask(__name__)
app.secret_key = 'should be changed'

app.config['SQLALCHEMY_DATABASE_URI']='postgres://gkuebhlmxhtjau:5e496cb9299ee89363d408be21367dab4dd1745fb45bed374f8a787bad39fd7c@ec2-52-2-82-109.compute-1.amazonaws.com:5432/d349hchhak43qj'
db = SQLAlchemy(app)

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
        return "Logged in successfully!!"
    return render_template("login.html", form=login_form)

    
#always true
if __name__ == "__main__":
    app.run(debug=True)