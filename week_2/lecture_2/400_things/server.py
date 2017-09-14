from flask import Flask, render_template, redirect, request, session, url_for, flash, get_flashed_messages
app = Flask(__name__)

app.secret_key = "supersecretkey"

@app.route('/')
def index():
    print get_flashed_messages()
    css_file = url_for('static', filename='style.css')
    return render_template("index.html", style=css_file)

@app.route('/process', methods=['POST'])
def process():
    print type(request.form['name'])
    # make sure all fields are filled
    if len(request.form['name']) < 1 or len(request.form['location']) < 1:
        flash("All fields are required")
        return redirect('/')
    else:
        print "success"

    try:
        session['users']
    except KeyError:
        session['users'] = []

    temp = session['users']
    temp.append(request.form)
    session['users'] = temp

    return redirect('/')

app.run(debug=True)
