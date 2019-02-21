import requests
import os
from math import *

API_BASE_URL = "https://api.uwaterloo.ca/v2"

class UWaterloo:
    def __init__(self, api_key):
        self.api_key = api_key
        self.course_count = 0.0
        self.current_count = 0.0

    def get_courses(self):
        payload = {
            'key': self.api_key
        }
        
        resp = requests.get(API_BASE_URL + "/courses.json", params=payload)

        if resp.status_code != 200:
            print("ERROR, response status code: {}".format(resp.status_code))
            return []

        courses = []

        for course_data in resp.json()['data']:
            courses.append({
                'course_name': '{0}{1}'.format(course_data['subject'], course_data['catalog_number']),
                'course_title': course_data['title']
            })

        self.course_count = len(courses)

        return courses