from flask import Flask, render_template

from wtform_fields import *
from models import *

app  = Flask(__name__)
app.secret_key = 'should be changed'

app.config['SQLALCHEMY_DATABASE_URI']='postgres://gkuebhlmxhtjau:5e496cb9299ee89363d408be21367dab4dd1745fb45bed374f8a787bad39fd7c@ec2-52-2-82-109.compute-1.amazonaws.com:5432/d349hchhak43qj'
db = SQLAlchemy(app)

@app.route("/", methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password  =reg_form.password.data

        # if user name exists        
        user_object = User.query.filter_by(username=username).first()
        if user_object:
            return "Already existing username!"

        #adding user to db
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "Inserted in to the db"


    return render_template("index.html", form=reg_form)
    
#always true
if __name__ == "__main__":
    app.run(debug=True)