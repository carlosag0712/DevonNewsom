from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "somesupersecretkey"

# http://127.0.0.1:5000/
@app.route('/')
def index():
    try:
        print session['user']
    except KeyError:
        print "no user yet"
    
    return render_template("index.html")

@app.route('/friends')
def friends():
    friends = [
        "tashon",
        "bianca",
        "patrick",
        "jenna",
        "joao",
        "tim"
    ]
    return render_template("friends.html", names=friends)

@app.route("/<friend>")
def one_friend(friend):
    print friend
    return friend

@app.route('/form_submit', methods=['POST'])
def form_handling():
    session['user'] = request.form['username']
    return redirect('/')

app.run(debug=True)