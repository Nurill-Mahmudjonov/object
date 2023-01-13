class Student:
    """we creat a class named Student"""

    def __init__(self, firstName, lastName, birthday):
        """Student's features"""
        self.firstName = firstName
        self.lastName = lastName
        self.birthday = birthday
        self.course = 1

    def get_info(self):
        """student is about information"""
        return f"Firstname={self.firstName}\nLastname={self.lastName}\nBirthday={self.birthday}\nCourse={self.course}"

    def set_course(self, course):
        """a mothed that updates a student's course"""
        self.course = course

    def update_course(self, course):
        """multiply the student stage by one"""
        self.course += 1


class Science:
    def __init__(self, name):
        self.name = name
        self.students_count = 0
        self.students = []

    def add_student(self, student):
        """add students to science"""
        self.students.append(student)
        self.students_count += 1

    def get_student(self):
        return [student.get_info() for student in self.students]

    def see_methods(klass):
        return [method for method in dir(klass) if not method.startswith('__')]


print(Science.see_methods(Student))
