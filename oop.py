class Student:
    def __init__(self, name, age, subj):
        self.name=name
        self.age=age
        self.subj=subj
    def info(self):
        return f"Student name is {self.name}. His age is {self.age} and subject is {self.subj}"


firstStudent = Student("Ali", 20, "English")
print(firstStudent.info())
secondStudent = Student("Ahmad", 15, "CS")
print(secondStudent.info())