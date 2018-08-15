from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register.sqlite3'

db = SQLAlchemy(app)
class students(db.Model):
   id = db.Column('reg_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   password = db.Column(db.String(50))

def __init__(self, name, password):
   self.name = name
   self.passowrd =password