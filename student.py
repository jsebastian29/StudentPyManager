students = []

class Student:

    # Class attributes
    school_name = "Springfield Elementary"
    #Pass keyword for doing nothing
    #__init__ constructor method
    def __init__(self, name, student_last_name, student_id=3332):
        
        """
        Constructor method that adds a new student
        :param name: string - student name
        :param student_id: integer - optional student ID
        """
        
        # Instance attributes
        self.name = name
        self.student_id = student_id
        self.last_name = student_last_name
        students.append(self)

    #Called when printing instance of the class
    def __str__(self):
        return "Student " + self.name


    def get_name_capitalize(self):
        return self.name.capitalize()


    def get_school_name(self):
        return self.school_name