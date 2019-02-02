from flask import request
import traceback

from flask_restful import Resource
from app.Model import db, Course, CourseSchema
from flask_restful import Resource,reqparse
import json,sys,os
sys.path.insert(0, '../')
from app.scripts.pdfparser import PdfParser
sys.path.insert(0, './endpoints')


class TranscriptParserResource(Resource):
    # CHANGE, no longer a get request
    def get(self):
        
        return {
            'status': 'error',
            'data': 'no get requests'
            }, 200

    def post(self):
        file = request.files['file']
        userUUID = request.args.get('uuid')
        filename = '{}transcript.pdf'.format(userUUID)
        file.save(os.path.join('./app/scripts', filename))
        try:
            parsedTranscript = PdfParser(filename)
            return {
                'status': 'success',
                'data': parsedTranscript
                    }, 200
        except:
            
            return {
                'status': 'error',
                'data': 'failed to parse'
                }, 200