from flask import request
from flask_restful import Resource
from app.Model import db, Course, CourseSchema
import json

courses_schema = CourseSchema(many=True)
course_schema = CourseSchema()

class PostReqResource(Resource):
    def get(self):
        courses = {}
        try:
            # TODO Replace code below, this was just copied from Courses.py
            raise ValueError('Using to skip try block.')
            courses = Course.query.all()
            courses = course_schema.dump(courses).data
        except:
            with open('./app/JSON/postreq.json') as f:
                courses = json.load(f)
        return {
            'status': 'success',
            'data': courses
        }, 200

    def post(self):
        return {
            'message': 'Post mesages not accepted!'
        }