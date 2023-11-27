from flask import Flask,render_template,request
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)
app.route("/")
def func():
    return render_template("index.html")
app.route("/register")
def func_1():
    return render_template("register.html")
app.route("/login")
def func_2():
    return render_template("login.html")
app.route("/registerprocess")
def func_reg_pros():
    client = MongoClient()
    uri = "mongodb+srv://madhan22012003:ncMG56zKqFRU69AL@teachermanagement.njy5gmr.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client.TeacherDatabase
    j=request.form['username']
    db.Project.insert_one({'username': j,'password': request.form['password'],'age': request.form['age'],'dob': request.form['dob'],'contact' : request.form['contact']})
    k=db.Project.find({'username':j})
    return render_template("profile.html",i=k)
app.route("/loginprocess")
def func_log_pros():
    client = MongoClient()
    uri = "mongodb+srv://madhan22012003:ncMG56zKqFRU69AL@teachermanagement.njy5gmr.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client.TeacherDatabase
    k=db.Project.find({'password': request.form['password']})
    return render_template("profile.html",i=k)
app.route("/")
if __name__ == '__main__':
    app.run(debug=True)
