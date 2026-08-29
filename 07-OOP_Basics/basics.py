# # BASIC CLASS & OBJECTS
# # Created a class then create an object

# class Student:
#     pass
# student1 = Student() #object
# student2 = Student() #object

# print(student1)
# print(student2)

# # GIVE OBJETCS DATA
# # Attributes = a simple piece of information/data that belongs to an object.

# class Student:
#     pass
# student1 = Student()
# student1.name = "Sim Akhter"
# student1.age = 20
# print(student1.name)
# print(student1.age)



# # MULTIPLE OBJECTS
# class Student:
#     pass
# student1 = Student()
# student2 = Student()
# student1.name = "Sim AKhter"
# student1.age = 20

# student2.name = "Aayushi Banerjee"
# student2.age = 19

# print(student1.name, student1.age)
# print(student2.name, student2.age)



# #CONSTRUCTORS
# class Student:

#     #default constructors
#     def __init__(self):
#         pass

#     #parameterized constructors
#     def __init__ (self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("Adding new student in DataBase.")

# s1 = Student("Sim Akhter", 96)
# print(s1.name, s1.marks)

# s2 = Student("Sehaam Seikh", 100)
# print(s2.name, s2.marks)



# # CREATE STUDENT CLASS THAT TAKES NAME & MARKS OF THREE SUBJECTS AS ARGUMENTS IN CONSTRUCTOR. THEN CREATE A METHOD TO PRINT THE AVERAGE.
# class Student:
#     def __init__(self, name,marks):
#         self.name = name
#         self.marks = marks
    
#     @staticmethod
#     def hello():
#         print("HElloww!") 

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print(self.name, "secured on an average", sum/3)

# s1 = Student("Sim AKhter", [98, 96, 75])
# s1.get_avg()
# s1.hello()



# # ABSTRACTION EXAMPLE
# class Car:
#     def __init__ (self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
    
#     def start(self):
#         self.clutch = True           
#         self.acc = True
#         print("car started...vroommm")

# car1 =Car()
# car1.start()



# # CREATE ACCOUNT CLASS WITH 2 ATTRIBUTES - BALANCE AND ACCOUNT NO. CREATE METHODS DOR DEBIT, CREDIT AND PRINTING THE BALANCE
# class Account:
#     def __init__(self, balance, acc_no):
#         self.balance = balance
#         self.acc_no = acc_no
    
#     def debit(self, amount):
#         self.balance -= amount
#         print("RS.", amount, "debited.")
#         print("Total balance = ", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("RS.", amount, "credited.")
#         print("Total balance = ", self.get_balance())

#     def get_balance(self):
#          return self.balance

# acc1 = Account(10000, 12345)
# acc1.debit(1000)
# acc1.credit(500)



# INHERITANCE
class Car:
    colour = "Black"
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped....")

class ToyotaCar(Car):
    def __init__ (self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

print(car1.colour)
print(car2.start())
print(car1.stop())