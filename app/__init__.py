from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask import session

app = Flask(__name__)
app.config['SECRET_KEY'] = "@#$%my$ecretKey@#$%*"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ldeeolffifzwrh:f964dc6f33fdbaf21381\
0db7cb63927883136874f3338c595560d062a9ba046b@ec2-54-221-201-212.compute-1.amazonaws.com:5432/d8h7mmdiiajgrm' #"postgresql://project1:project1@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
UPLOAD_FOLDER = './app/static/uploads'

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views