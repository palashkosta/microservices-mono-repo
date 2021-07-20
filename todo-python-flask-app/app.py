from dataclasses import dataclass
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='mysql://root:root@db/db_todo'
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@dataclass
class Todo(db.Model):
    id: int
    title: str
    description: str

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(200))

@app.route('/api/todos', methods=['GET'])
def get_todo():
    return jsonify(Todo.query.all())

@app.route('/api/todo', methods=['POST'])
def post_todo():
    ## getting the data from request
    data = request.json

    ## extracting the data as individual fields
    id = data['id']
    title = data['title']
    description = data['description']

    ## adding to db
    try:
        postedTodo = Todo(id=id,title=title, description=description)
        db.session.add(postedTodo)
        db.session.commit()
    except:
        abort(400, 'You already have this todo')
    
    return jsonify({
        'code': 200,
        'message': 'success -> added todo with id ' + str(postedTodo)
    })

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
