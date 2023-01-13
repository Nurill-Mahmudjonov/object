class Student:
    """we creat a class named Student"""

    def __init__(self, firstName, lastName, birthday, course):
        """Student's features"""
        self.firstName = firstName
        self.lastName = lastName
        self.birthday = birthday
        self.course = 1

    def get(self):
        return f"Firstname={self.firstName}\nLastname={self.lastName}\nBirthday={self.birthday}\nCourse={self.course}"


list = Student.get()
print(list)
