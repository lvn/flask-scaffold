from flask.ext.sqlalchemy import SQLAlchemy
from app import db

# Models go here.
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64))
	password = db.String(db.String(64))
	email = db.String(db.String(256))