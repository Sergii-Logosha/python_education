class Student:

    def __init__(self, student_id, name, age, gpa):
        self.student_id = student_id
        self.name = name
        self._age = age
        self.gpa = gpa


student_nora = Student("234AFE", "Nora Navone", 15, 3.96)

print(student_nora._age)
