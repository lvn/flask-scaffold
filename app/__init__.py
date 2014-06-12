import os
from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.oauth import OAuth
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')
app.config.update(dict(
	DATABASE=os.path.join(app.root_path, 'app.db'),
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.root_path, 'data/app.db'),
	SQLALCHEMY_MIGRATE_REPO=os.path.join(app.root_path, 'app_db_repo'),
	DEBUG=True))

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

db.create_all()
lm = LoginManager()
lm.init_app(app)
oauth = OAuth()

from app import views, models