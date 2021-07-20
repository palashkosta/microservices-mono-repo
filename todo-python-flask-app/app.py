from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='mysql://root:root@db/db_todo'
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(200))

@app.route('/')
def index():
    return "Hellow"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
