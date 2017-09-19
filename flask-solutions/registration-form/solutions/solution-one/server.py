from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key = "sessionkey"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# Ninja Version
PASSWORD_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?[0-9])')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def process():
    errors = False

    if len(request.form['first_name']) == 0:
        flash('First Name cannot be blank', 'error')
        errors = True

    elif not request.form['first_name'].isalpha():
        flash('First Name cannot contain numbers or special characters', 'error')
        errors = True

    if len(request.form['last_name']) == 0:
        flash('Last Name cannot be blank', 'error')
        errors = True

    elif not request.form['last_name'].isalpha():
        flash('Last Name cannot contain numbers or special characters', 'error')
        errors = True

    if len(request.form['password']) < 8:
        flash('Password must be at least 8 characters', 'error')
        errors = True

    elif not PASSWORD_REGEX.match(request.form['password']):
        flash('Password must contain at least one uppercase letter and one number', 'error')
        errors = True

    elif request.form['password'] != request.form['c_password']:
        flash('Passwords must match', 'error')
        errors = True

    if len(request.form['email']) == 0:
        flash('Email cannot be blank', 'error')
        errors = True

    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Email is not valid', 'error')
        errors = True

    if not errors:
        flash('Successful Registration!', 'success')

    return redirect('/')

app.run(debug=True)
