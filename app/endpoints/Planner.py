from flask import request
from flask_restful import Resource,reqparse
from app.scripts.PlannerLogic import PlannerLogic
from app.Model import db, Course, CourseSchema
import json, jsonify

courses_schema = CourseSchema(many=True)
course_schema = CourseSchema()

class PlannerResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('course', action='append')
        coursesInput = parser.parse_args()
        # coursesInput['course'] returns a list of all courses input
        futureCourses = PlannerLogic(coursesInput['course'])
        response= {
            'Access-Control-Allow-Origin':'*',
            'status': 'success',
            'data': futureCourses
        }
        response.jsonify.headers.add('Access-Control-Allow-Origin', '*') 
        return (response,200)

    def post(self):
        return {
            'message': 'Post mesages not accepted!'
        }