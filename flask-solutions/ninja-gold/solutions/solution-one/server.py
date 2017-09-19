from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random
app = Flask(__name__)
app.secret_key = "sessionkey"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
    return render_template("index.html", gold=session['gold'], activities=session['activities'])

@app.route('/process_money', methods=['POST'])
def process_money():
    time = datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
    # print time
    building = request.form['building']
    if building == 'farm':
        gold = random.randrange(10,20+1)
        session['activities'].append({'activity':"You entered a {} and earned {} golds".format(building, gold), 'class':'win', 'date':time})

    elif building == 'cave':
        gold = random.randrange(5,10+1)
        session['activities'].append({'activity': "You entered a {} and earned {} golds".format(building, gold), 'class':'win', 'date':time})

    elif building == 'house':
        gold = random.randrange(2,5+1)
        session['activities'].append({'activity': "You entered a {} and earned {} golds".format(building, gold), 'class':'win', 'date':time})

    elif building == 'casino':
        gold = random.randrange(-50,50+1)
        if gold < 0:
            session['activities'].append({'activity': "You entered a {} and lost {} golds".format(building, gold), 'class': 'loss', 'date':time})
        else:
            session['activities'].append({'activity': "You entered a {} and earned {} golds".format(building, gold), 'class':'win', 'date':time})

    session['gold'] += gold
    return redirect('/')

app.run(debug=True)
