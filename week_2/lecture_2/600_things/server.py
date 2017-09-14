from flask import Flask, render_template, redirect, session, request, flash, get_flashed_messages

app = Flask(__name__)

app.secret_key = "secrettsss"

@app.route('/')
def index():
    
    return render_template("index.html", messages=get_flashed_messages())

@app.route('/reset')
def clear():
    session.clear()
    return redirect('/')

@app.route('/process', methods=["POST"])
def process_form():
    try:
        session['foods']
    except KeyError:
        session['foods'] = []

    # validations!!!!!!!!

    # field is required
    if len(request.form['food'].strip()) < 1:
       flash("invalid!!!! field is required")

    # the food is a duplicate
    elif request.form['food'] in session['foods']:
        flash("invaid! the food is a duplicate")

    else:
        temp_foods = session['foods']
        temp_foods.append(request.form['food'])
        session['foods'] = temp_foods
        session['food'] = request.form['food']
    return redirect('/')

app.run(debug=True)