class Student:
    school ="ABC School"
    # blueprint
    def __init__(self, name, marks, attendance):
        self.name = name
        self.marks = marks
        self.attendance = attendance

    def calculate_grade(self):
            if self.marks >= 90:
                return "A"
            elif self.marks<=80:
                return "B"
            else:
                return "C"

s1 = Student("sachin", 90, 85)
print(s1.name)
print(s1.calculate_grade())
s2 = Student("sourav", 85, 90)
print(s2.name)

s3 = Student("virat", 95, 80)
print(s3.name)
print(Student.school)

# print(s1.attendance)
# print(s2.attendance)
# print(s3.attendance)

# print(s1.attendance)
# print(s2.attendance)
# print(s3.attendance)

