from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///splitwise.db'
db = SQLAlchemy(app)


if __name__ == "__main__":
    from views import *
    app.run(debug=True)