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
    
    def get(self):
        return {
            'status': 'error',
            'data': 'Get requests not accepted'
            }, 400

    def post(self):
        file = request.files['file']
        userUUID = request.args.get('uuid')
        filename = '{}transcript.pdf'.format(userUUID)
        file.save(os.path.join('./app/scripts', filename))
        try:
            parsedTranscript = PdfParser(filename)
            # prob some python magic to make the code below look nicer
            data =[]
            for x in range(0,len(parsedTranscript[0])):
                data.append( (parsedTranscript[0][x] + parsedTranscript[1][x]).replace(" ", "") )
            return data,200
        except:
            
            return {
                'status': 'error',
                'data': 'failed to parse'
                }, 500