from flask import Flask, render_template

app  = Flask(__name__)
app.secret_key = 'should be changed'

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")
    
#always true
if __name__ == "__main__":
    app.run(debug=True)