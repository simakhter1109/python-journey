# # CLASS & OBJECT
# class Student:
#     name = "Sim"
#     age = 20
# student1 = Student()
# print(student1.name)
# print(student1.age)


# MULTIPLE OBJECTS
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("Sim", 20)
student2 = Student("Sahil", 22)
print(student1.name)
print(student2.age)