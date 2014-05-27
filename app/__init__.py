from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.oauth import OAuth

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
db.create_all()
lm = LoginManager()
lm.init_app(app)
oauth = OAuth()

from app import views, models