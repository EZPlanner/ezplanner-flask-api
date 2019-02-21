from flask import request
from flask_restful import Resource
from app.Model import db, Course, CourseSchema
import json

courses_schema = CourseSchema(many=True)
course_schema = CourseSchema()

class CoursesResource(Resource):
    def get(self):
        courses = {}

        courses = Course.query.all()
        courses = courses_schema.dump(courses).data

        return {
            'status': 'success',
            'data': courses
        }, 200