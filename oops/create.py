class Student:
    # blueprint
    def __init__(self, name, rollno, attendance):
        self.name = name
        self.rollno = rollno
        self.attendance = attendance


s1 = Student("sachin", 1, 90)
print(s1.name)

s2 = Student("sourav", 2, 85)
print(s2.name)

s3 = Student("virat", 3, 95)
print(s3.name)
print(s1.attendance)
print(s2.attendance)
print(s3.attendance)

print(s1.attendance)
print(s2.attendance)
print(s3.attendance)

