from flask import Blueprint
from flask_restful import Api
from app.endpoints.Courses import CoursesResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(CoursesResource, '/courses')