from flask import request, jsonify
from flask_restful import Resource,reqparse
from app.scripts.PlannerLogic import PlannerLogic
from app.Planner import Planner
from app.Model import db, Course, CourseSchema
import json

courses_schema = CourseSchema(many=True)
course_schema = CourseSchema()

class PlannerResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('course', action='append')
        coursesInput = parser.parse_args()

        courses = {}

        courses = Course.query.all()
        courses = courses_schema.dump(courses).data

        title_map = {}

        for course in courses:
            title_map[course['course_name']] = course['course_title']

        planner = Planner(coursesInput['course'], title_map)

        # coursesInput['course'] returns a list of all courses input
        futureCourses = planner.get_possible_courses()
        
        
        return futureCourses, 200