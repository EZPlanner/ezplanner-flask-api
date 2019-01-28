from flask import Blueprint
from flask_restful import Api
from app.resources.Course import CourseResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(CourseResource, '/course')