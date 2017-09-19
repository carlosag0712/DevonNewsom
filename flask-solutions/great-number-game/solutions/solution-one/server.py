from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "keep_it_secret_keep_it_safe"

@app.route('/')
def index():
    if 'target' not in session:
        session['target'] = random.randint(1,100)
    return render_template('index.html')

@app.route('/guess', methods=["POST"])
def guess():
    if session['target'] == int(request.form['guess']):
        # show reset somehow
        session['result'] = 'correct'

    elif session['target'] < int(request.form['guess']):
        # you're too high
        session['result'] = 'high'

    else:
        # you're too low
        session['result'] = 'low'

    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('target')
    session.pop('result')
    return redirect('/')

app.run(debug=True)