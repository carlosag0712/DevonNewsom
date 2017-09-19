from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "sessionkey"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    errors = False
    if len(request.form['name']) == 0:
        flash('Name must not be blank')
        errors = True
    if len(request.form['comment']) == 0:
        flash('Comment must not be blank')
        errors = True
    if len(request.form['comment']) > 120:
        flash('Comment can not be over 120 characters')
        errors = True
    if errors:
        return redirect('/')
    
    #using session to persist the form data so we can redirect to another route
    session['submitted_info'] = request.form 
    return redirect('/result')

@app.route('/result')
def success():
    return render_template("result.html", result=session['submitted_info'])

app.run(debug=True)
