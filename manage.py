#!/usr/bin/env python
import os
from app import app, db
from app.models import User
from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

server = Server(host="0.0.0.0", port=8000)


def make_shell_context():
    return dict(app=app, db=db, User=User)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', server)

from app import views

if __name__ == '__main__':
    manager.run()
