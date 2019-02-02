#!python3
""" JSON reader

Requirements: python3

Description:
    This python file will create a list of courses you may take given a list of courses you have completed.

Usage:
    python3 planner.py <filename>.txt

Disclaimer:
    There are edge cases to consider such as CLAS361 which have an empty parsed list

"""

def PlannerLogic(courses):
    import json,re

    with open('./app/JSON/courses.json') as f:
        coursesDict = json.load(f)

    with open('./app/JSON/prereq.json') as f:
        prereqDict = json.load(f)

 
    with open('./app/JSON/postreq.json') as f:
        postreqDict = json.load(f)

    possible_courses = []       # courses you might be able to take
    allowed_courses = []        # courses you are allowed to take 


    for course in courses:
        if course in postreqDict:
            possible_courses.extend(postreqDict[course])

    possible_courses = list(set(possible_courses)) #removes duplicates 

    # checks if you have the nececcary prereq's for the course.
    # returns true or false
    def check_prereq(course):
        # get parsed prereq's
        prereqs = prereqDict[course]
        # print("Checking {}".format(course))
        return recursive_check(prereqs)

    def recursive_check(items):
        counter = 0
        count_to = 0
        for item in items:
            
            if isinstance(item, list):
                if recursive_check(item) == False:
                    return False
            if isinstance(item, int):
                count_to = item
            else:
                if item not in courses and count_to == 0:
                    return False
                elif item in courses:
                    counter+=1
        if count_to > 0 and counter < count_to:
            return False
        else:
            return True
    # TODO optimize code below
    def findTitle(course):
        courseSplit = (re.split(r'(^[^\d]+)', course)[1:])
        for course in coursesDict['data']:
            if  courseSplit[0] == course['subject'] and courseSplit[1] == course['catalog_number']:
                return course['title']
        return 'null'
    # check prereq's of each possible course
    for course in possible_courses:
            if check_prereq(course):
                if course not in courses:
                    courseTitle = findTitle(course)
                    toAdd = [course, courseTitle] 
                    allowed_courses.append(toAdd)

    
    return allowed_courses
