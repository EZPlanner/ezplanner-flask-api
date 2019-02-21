import os

from flask_script import Manager
from app.Model import db, Course
from app import create_app
from app.uwaterloo import UWaterloo

app = create_app('config')

manager = Manager(app)

@manager.command
def db_seed():
    uw = UWaterloo(os.environ['UW_API_KEY0'])
    courses = uw.get_courses()

    db.engine.execute(Course.__table__.insert(), courses)

if __name__ == '__main__':
    manager.run()