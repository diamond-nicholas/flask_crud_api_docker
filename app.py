from distutils.log import debug
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

if __name__ == '__main__':
 app.run(debug=True)

app.config['SQLAlCHEMY_DATABASE_URI']= os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)


class Item(db.model):
 id = db.Column(db.integer, primary_key=True)
 title= db.Column(db.String(80), unique=True, nullable=False)
 content= db.Column(db.String(120), unique=True, nullable=False)

 def __init__(self, title, content):
  self.title = title
  self.content = content

db.create_all()