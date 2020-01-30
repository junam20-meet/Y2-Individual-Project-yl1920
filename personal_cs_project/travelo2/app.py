from flask import Flask
from flask import render_template
from database import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html",  EXPLAIN_TEMPLATE_LOADING=True)

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email_address']
        passcode = request.form['passcode']
        database.add_user(name,email_address,passcode)
        return render_templete("login.html")
    else:
        return render_templete("sign_up.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = databases.query_by_name(request.form["username"])
        print(request.form['username'])
        if user is not None:
            if user.password == request.form["password"]:
                session['username'] = user.username
                return redirect(url_for("home", username = user.username))
            else:
                error = 'password does not match'
                return render_template('home.html', error = error)
        else:
            error = 'username does not exist'
            return render_template('home.html', error = error)
    else:
        return render_template('login.html')
    


if __name__ == '__main__':
    app.run(debug=True)
