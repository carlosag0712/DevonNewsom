from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnector
from datetime import datetime
app = Flask(__name__)

mysql = MySQLConnector(app, "mydb")

@app.route('/')
def index():
    all_my_friends = mysql.query_db("SELECT * FROM friends;")
    return render_template('index.html', friends=all_my_friends)

@app.route('/<friend_id>')
def show(friend_id):
    query_string = "SELECT * FROM friends WHERE id = :some_id"
    data_dictionary = {"some_id": friend_id}
    try:
        one_friend = mysql.query_db(query_string, data_dictionary)[0]
    except IndexError:
        return redirect('/')
    return render_template('show.html', friend=one_friend)

@app.route('/<friend_id>/edit')
def edit(friend_id):
    query_string = "SELECT * FROM friends WHERE id = :some_id"
    data_dictionary = {"some_id": friend_id}
    try:
        one_friend = mysql.query_db(query_string, data_dictionary)[0]
    except IndexError:
        return redirect('/')
    return render_template('edit.html', friend=one_friend)

@app.route('/new')
def new():
    return render_template("new.html")

@app.route('/<friend_id>/update', methods=['POST'])
def update(friend_id):
    query_string = "UPDATE friends SET username = :updated_username,\
                                       updated_at = :now \
                    WHERE id = :some_id"
    data_dictionary = {
        "updated_username": request.form['username'],
        "now": datetime.now(),
        "some_id": friend_id
    }
    mysql.query_db(query_string, data_dictionary)
    return redirect('/')

@app.route('/create', methods=['POST'])
def create():
    query_string = "INSERT INTO friends (username, created_at, updated_at)\
                    VALUES (:new_username, NOW(), NOW())"
    data_dictionary = {
        "new_username": request.form['username']
    }
    new_friend_id = mysql.query_db(query_string, data_dictionary)
    
    return redirect('/{}'.format(new_friend_id))

@app.route('/<friend_id>/delete')
def delete(friend_id):
    query_string = "DELETE FROM friends WHERE id = :some_id"
    data_dictionary = {"some_id": friend_id}
    mysql.query_db(query_string, data_dictionary)
    return redirect('/')

app.run(debug=True)
