from flask import request, jsonify
from flask_restful import Resource,reqparse
from app.scripts.PlannerLogic import PlannerLogic
from app.Planner import Planner
import json

class PlannerResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('course', action='append')
        coursesInput = parser.parse_args()

        title_map = {}

        with open('./courses_title.json') as f:
            title_map = json.load(f)

        planner = Planner(coursesInput['course'], title_map)

        # coursesInput['course'] returns a list of all courses input
        futureCourses = planner.get_possible_courses()
        
        
        return futureCourses, 200