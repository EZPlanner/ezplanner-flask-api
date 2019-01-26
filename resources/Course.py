from flask import request
from flask_restful import Resource
from Model import db, Course, CourseSchema

courses_schema = CourseSchema(many=True)
course_schema = CourseSchema()

class CourseResource(Resource):
    def get(self):
        courses = Course.query.all()
        courses = course_schema.dump(courses).data

        return {
            'status': 'success',
            'data': courses
        }, 200

    def post(self):
        return {
            'message': 'Hello, World!'
        }