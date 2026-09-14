# # CLASS & OBJECT
# class Student:
#     name = "Sim"
#     age = 20
# student1 = Student()
# print(student1.name)
# print(student1.age)


# # MULTIPLE OBJECTS
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# student1 = Student("Sim", 20)
# student2 = Student("Sahil", 22)
# print(student1.name)
# print(student2.age)



# # CONSTRUCTOR
# class Student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
# student = Student ("Sahil", 22, 96)
# print(student.name)
# print(student.age)
# print(student.marks)


# # METHODS
# class Student:
#     def __init__ (self, name):
#         self.name= name
#     def introduce(self):
#         print(f"Hi, I am {self.name}.")
# student = Student("Sahil")
# student.introduce()




# # STUDENT GRADE SYSTEM (class + object + constructor + methods + attributes)
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def average(self):
#         return sum (self.marks)/ len(self.marks)

#     def grade(self):
#         avg = self.average()
#         if avg >= 90:
#             return "A"
#         elif avg >= 80:
#             return "B"
#         elif avg >= 70:
#             return "C"
#         elif avg >= 60:
#             return "D"
#         else:
#             return "F"
# student1 = Student("Sim", [86, 90, 78, 93])
# student2 = Student("Sahil", [89, 98, 87, 95])
# print("Student 1: ")
# print(student1.name)
# print(student1.average())
# print(student1.grade())
# print("Student 2: ")
# print(student2.name)
# print(student2.average())
# print(student2.grade())

 


# # ENCAPSULATION
# class BankAccount:
#     def __init__ (self, balance):
#         self.__balance = balance
#     def deposite (self, amount):
#         self.__balance += amount
#     def show_balance(self):
#         print("Balance: ", self.__balance)
# account = BankAccount(5000)
# account.deposite(2000)
# account.show_balance()




# # INHERITANCE
# class Animal:
#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")
# dog = Dog()
# dog.eat()
# dog.bark()
# # here Dog inherits from Animal ... Animal - Parent class
# # Dog - Child class



# POLYMORPHISM
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog says Woof!")
dog = Dog()
dog.sound()