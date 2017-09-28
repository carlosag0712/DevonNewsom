from flask import Flask, render_template, redirect, request, flash, get_flashed_messages, url_for, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.secret_key = "lol"
mysql = MySQLConnector(app, "mydb")

def get_user_from_id(id):
    query = "SELECT * FROM friends WHERE id = :id"
    return mysql.query_db(query, {"id": id})[0]

@app.route('/')
def index():
    flash_messages = get_flashed_messages(with_categories=True)
    staticfile = url_for('static', filename="style.css")
    return render_template("index.html", 
                            messages = flash_messages, 
                            styles = staticfile)

@app.route('/register', methods=['POST'])
def register():
    errors = []

    # min length on username
    if len(request.form['username']) < 5:
        errors.append("Username must be 5 or more characters long")

    # min length on password
    if len(request.form['password']) < 8:
        errors.append("Password must be 8 or more characters long")        

    # password matches
    if request.form['password'] != request.form['confirm_password']:
        errors.append("Passwords do not match")

    # unique username
    query = "SELECT id FROM friends WHERE username = :some_username"
    data = {"some_username": request.form['username']}
    # check list for items
    if mysql.query_db(query, data):
        errors.append("Username already taken!")
    

    # check errors list
    if errors:
        #flash each error in list, then redirect
        for e in errors:
            flash(e, "error")
        return redirect("/")

    hashed = bcrypt.generate_password_hash(request.form['password'])

    # create a user
    query = "INSERT INTO friends (username, password)\
             VALUES (:some_username, :some_password)"
    data = {
        "some_username": request.form['username'],
        "some_password": hashed 
    }
    mysql.query_db(query, data)
    flash("Successfully Registered", "success")
    return redirect("/")

@app.route("/login", methods=['POST'])
def login():
    errors = []
    # check DB for username
    query = "SELECT id, password FROM friends WHERE username = :some_username"
    data = {"some_username": request.form['username']}
    # find friend with that username
    # check list for items
    friend = mysql.query_db(query, data)[0]
    if not friend:
        errors.append("Invalid username/password")
    # if username, check_pw_hash
    else:
        if not bcrypt.check_password_hash(friend["password"], request.form['password']):
            errors.append("Invalid username/password")

    if errors:
        #flash each error in list, then redirect
        for e in errors:
            flash(e, "error")
        return redirect("/")

    # save id to session
    session['id'] = friend['id']
    flash("Successfully Logged in", "success")
    return redirect("/success")

# LOGIN PROTECTED SITE
@app.route('/success')
def success():
    # check session for 'id'
    try:
        session['id']
    except KeyError:
        return redirect('/')

    user = get_user_from_id(session['id'])
    flash_messages = get_flashed_messages(with_categories=True)

    return render_template("success.html", user = user, messagse = flash_messages)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


app.run(debug=True)
