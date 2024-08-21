# Create a roster of students by grade

class School:
    def __init__(self):
        self.school_roster = dict()
        self.check = []

    def add_student(self, name, grade):
        if name not in self.school_roster:
            self.school_roster[name] = grade
            # self.school_roster[grade].append(name)
            self.check.append(True)
        else:
            self.check.append(False)
        
    def roster(self):
        # return self.roster
        self.school_roster = sorted(self.school_roster.items(), key=lambda x: (x[1],x[0])) # x[1],x[0]?
        return [x for x, grade in self.school_roster]  # x for x?

    def grade(self, grade_number):
        # result is calculated out of the return statement to make it easier to troubleshoot
        result = sorted([key for key, value in self.school_roster.items() if value == grade_number])
        return result

    def added(self):
        return self.check
