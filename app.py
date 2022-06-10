from distutils.log import debug
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

if __name__ == '__main__':
 app.run(debug=True)

app.config['SQLAlCHEMY_DATABASE_URI']= os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)


