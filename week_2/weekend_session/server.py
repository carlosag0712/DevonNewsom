from flask import Flask, render_template, redirect, session, flash, request, get_flashed_messages
import re
app = Flask(__name__)

app.secret_key = "secretkey"

NAME_PATTERN = re.compile(r"^[a-zA-Z]+$")
EMAIL_PATTERN = re.compile(r"^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$")

@app.route("/")
def index():
    messages = get_flashed_messages()
    return render_template("index.html", messages=messages)

@app.route("/register", methods=['POST'])
def register():
    print request.form

    # CHECK FIRST/LAST NAME FOR VALID STRING
    first_name_matches = re.match(NAME_PATTERN, request.form['first_name'].strip())
    last_name_matches = re.match(NAME_PATTERN, request.form['last_name'].strip())
    if not first_name_matches or not last_name_matches:
        flash("First and Last Name cannot contain any numbers")
    
    # CHECK EMAIL FOR VALID STRING
    if not re.match(EMAIL_PATTERN, request.form['email']):
        flash("Email should be a valid email")

    
    return redirect('/')

app.run(debug=True)