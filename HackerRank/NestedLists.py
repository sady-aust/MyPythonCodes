class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks


students = []
allMarks = []

n = int(input())

for i in range(n):
    name = input()
    marks = input()
    students.append(Student(name,marks))
    allMarks.append(marks)

allMarks.sort()

ansnames = []

for student in students:
    if(student.marks == allMarks[1]):
        ansnames.append(student.name)

ansnames.sort()

for aName in ansnames:
    print(aName)






