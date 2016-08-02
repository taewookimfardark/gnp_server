import os
from application import app
from application import db
from flask.ext.script import Manager
from flask.ext.migrate import Migrate
from flask.ext.migrate import MigrateCommand

manager = Manager(app)
migrate = Migrate(app=app, db=db)

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()

