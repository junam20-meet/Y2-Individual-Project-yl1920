from flask import Flask, render_template, url_for, redirect, request, session
from flask import render_template
import database
#from database import *


app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html",  EXPLAIN_TEMPLATE_LOADING=True)

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        database.add_user(username,password)
        return render_template("login.html")
    else:
        return render_template("sign_up.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = database.query_by_name(request.form["username"])
        print(request.form['username'])
        if user is not None:
            if user.password == request.form["password"]:
                session['username'] = user.username
                return redirect(url_for("index", username = user.username))
            else:
                error = 'password does not match'
                return render_template('login', error = error)
        else:
            error = 'username does not exist'
            return render_template('login.html', error = error)
    else:
        return render_template('login.html')
    


if __name__ == '__main__':
    app.run(debug=True)
