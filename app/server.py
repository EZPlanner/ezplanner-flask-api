from flask import Blueprint
from flask_restful import Api
from app.endpoints.Courses import CoursesResource
from app.endpoints.PreReq import PreReqResource
from app.endpoints.PostReq import PostReqResource
from app.endpoints.Planner import PlannerResource
from app.endpoints.TranscriptParser import TranscriptParserResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(CoursesResource, '/courses')
api.add_resource(PreReqResource, '/prereqs')
api.add_resource(PostReqResource, '/postreqs')
api.add_resource(PlannerResource, '/planner')
api.add_resource(TranscriptParserResource, '/parser')