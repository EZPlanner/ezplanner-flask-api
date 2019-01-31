from flask import Blueprint
from flask_restful import Api
from app.endpoints.Courses import CoursesResource
from app.endpoints.PreReq import PreReqResource
from app.endpoints.PostReq import PostReqResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(CoursesResource, '/courses')
api.add_resource(PreReqResource, '/prereqs')
api.add_resource(PostReqResource, '/postreqs')