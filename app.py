from distutils.log import debug
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

if __name__ == '__main__':
 app.run(debug=True)

app.config['SQLAlCHEMY_DATABASE_URI']= os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)


class Item(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 title= db.Column(db.String(80), unique=True, nullable=False)
 content= db.Column(db.String(120), unique=True, nullable=False)

 def __init__(self, title, content):
  self.title = title
  self.content = content



# create endpoints

@app.route('/items/<db>', methods=['GET'])
def get_item(id):
 item = Item.query.get(id)
 del item.__dict__['_sa_instance_state']
 return jsonify(item.__dict__)

@app.route('/items/', methods=['GET'])
def get_items():
 items = []
 for item in db.session.query(Item).all():
  del item.__dict__['_sa_instance_state']
  items.append(item.__dict__)
 return json(items)

@app.route('/items', methods=['POST'])
def create_item():
 body = request.get_json()
 db.session.add(Item(body['title'], body['content']))
 db.session.commit()
 return 'Item created'

@app.route('/items/<id>', methods=['PUT'])
def update_item(id):
 body = request.get_json()
 db.session.query(Item).filter_by(id=id).update(
   dict(title=body['title'], content=body['content'])
  )
 db.session.commit()
 return 'Item updated'

@app.route('/items/<id>', methods=['DELETE'])
def delete_item(id):
 db.session.query(Item).filter_by(id=id).delete()
 db.session.commit()
 return "item deleted"

db.create_all()