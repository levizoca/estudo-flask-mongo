from flask import Flask, render_template, request, session, redirect
from functools import wraps
from elasticsearch import Elasticsearch
import pymongo

app = Flask(__name__)
app.secret_key = 'super secret key'

es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])

client = pymongo.MongoClient("mongodb://%s:%s@mongo:27018/" % ('mongoadmin', 'password'))
db = client["flask-login"]
db2 = client["estabelecimentos"]

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap

from modules.user import routes
from modules.establishment import routes
from modules.es_establishment import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/toDoList')
@login_required
def toDoList():
    return render_template('toDoList.html')