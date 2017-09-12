# import Flask class from flask module
from flask import Flask, render_template, redirect, session, request

# save instace of Flask class to 'app'
app = Flask(__name__)
app.secret_key = "asdfasdfasdf"

def build_list():
    return [ x*2 for x in range(1,10) ]

@app.route('/')
def index():
    
    return render_template("index.html", names=build_list())

@app.route('/hello')
def hello():
    print "hello"
    return render_template('other_page.html')

@app.route("/set_session", methods=['POST'])
def set_session():
    session['user'] = request.form['username']
    return redirect('/')

# tell app to run on server
app.run(debug=True)
