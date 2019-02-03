from app.aws.dynamodb import DynamoDB

class Planner:
    def __init__(self, courses_taken, title_map):
        self.courses_taken = courses_taken
        self.db = DynamoDB()
        self.prereq_dict = {}
        self.postreq_dict = {}
        self._load_prereq_dict()
        self._load_postreq_dict()
        self.courses_set = set(courses_taken)

    def _load_postreq_dict(self):
        table = self.db.get_post_req_table()
        postreqs = self.db.get_all_entries(table)

        postreq_dict = {}

        for postreq in postreqs:
            postreq_dict[postreq['course_key']] = postreq['postreqs']

        self.postreq_dict = postreq_dict

    def _load_prereq_dict(self):
        table = self.db.get_pre_req_table()
        prereqs = self.db.get_all_entries(table)

        prereq_dict = {}

        for prereq in prereqs:
            prereq_dict[''.join(prereq['course_key'].split('/'))] = prereq['prereqs']

        self.prereq_dict = prereq_dict

    def check_prereqs(self, items):
        taken = 0
        required = 0

        for item in items:
            if isinstance(item, list) and recursive_check(item) == False:
                return False
            
            if isinstance(item, int):
                required = item
            else:
                if required == 0 and item not in self.courses_set:
                    return False

                taken += 1

        if required > 0 and taken < required:
            return False
        
        return True

    def get_possible_courses(self):
        if self.courses_taken is None or len(self.courses_taken) == 0:
            return []

        possible_courses = []
        allowed_courses = []

        for course in self.courses_taken:
            possible_courses.extend(self.postreq_dict[course])

        possible_courses = list(set(possible_courses)) # Get rid of duplicates

        for course in possible_courses:
            if course not in self.courses_set and self.check_prereqs(self.prereq_dict[course]):
                allowed_courses.append([course, title_map[course]])

        return allowed_courses