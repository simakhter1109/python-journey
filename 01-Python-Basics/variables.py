# STORE BASIC INFORMATION IN VARIABLES
name = "Sim"
age = 20
country = "India"
print(name)
print(age)
print(country)



# DIFFERENT TYPES OF VARIABLES
name = "Sim"
age = 20
height = 5.4
is_student = True

print(name)
print(age)
print(height)
print(is_student)

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))



# CHANGING THE VALUE OF A VARIABLE
age = 20
print(age)

age = 21
print(age)

age = 22
print(age)



# USING VARIABLES IN CALCULATIONS
price = 500
quantity = 1
total = price * quantity
print("price: ", price)
print("Quantity: ", quantity)
print("Total: ", total)



# MULTIPLE VARIABLES IN ONE LINE
name, age, city = "Sim", 20, "Delhi"
print(name, age, city)



# TAKING INPUT FROM THE USER
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Your name is: ", name)
print("Your age is: ", age)



# CALCULATE AGE NEXT YEAR

name = input("Enter your name: ")
age = int(input("Enter your age: "))
next_year_age = age + 1

print("Hello", name)
print("Your current age is", age)
print("Next year you will be", next_year_age)



# USING VARIABLES INSIDE A STRING
name = "Sim"
age = 20
course = "Python"
message = f"My name is {name}. I am {age} years old and I am learning {course}."
print(message)



# SWAPPING THE VALUES OF TWO VARIABLES
a = 10
b = 20
print("Before swapping: ")
print("a = ", a)
print("b = ", b)
a, b = b, a
print("After swapping: ")
print("a = ", a)
print("b = ", b)



# SIMPLE SHOPPING BILL
item = input("Enter the item name: ")
price = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))
total = price * quantity
print()
print("-----BILL-----")
print(f"Item: {item}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print(f"Total: {total}")

