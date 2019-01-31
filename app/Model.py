from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(250), nullable=False)
    course_title = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, course_name, course_title):
        self.course_name = course_name
        self.course_title = course_title

class CourseSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    course_name = fields.String(required=True)
    course_title = fields.String(required=True)
    creation_date = fields.DateTime()