class Student:
    def __init__(self,id,name,course):
        self.id=id
        self.name=name
        self.course=course
    def details(self):
        return f"student Id:{self.id} student Name:{self.name} course:{self.course}"
student1=Student(101,"keerthi","ECE")
print(student1.details())
