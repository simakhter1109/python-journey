# # ARITHMETIC OPERATORS
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Remainder:", a % b)
# print("Power:", a ** b)
# print("Floor Division:", a // b)



# # ASSIGNMENT OPERATORS
# score = int(input("Enter a number: "))

# print("Starting score is: ", score)

# score += 5
# print("After +5 = ", score)
# score -= 3
# print("After -3 = ", score)
# score *= 2
# print("After *2 = ", score)
# score += 10
# print("After +10 = ", score)
# score -= 10
# print("After -10 = ", score)



# # COMPARISON OPERATORS
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))

# print("a > b: ", a > b)
# print("a < b: ", a < b)
# print("a == b: ", a == b)
# print("a != b: ", a != b)
# print("a >= b: ", a >= b)
# print("a <= b: ", a <= b)



# # LOGICAL OPERATORS
# age = int(input("Enter the age: "))
# has_id = True
# is_student = False

# can_enter = age >= 18 and has_id
# student_discount = is_student or age < 18
# no_id = not has_id

# print("Can enter: ", can_enter)
# print("Student discount: ", student_discount)
# print("No valid ID: ", no_id)



# # GRADE CALCULAATOR
# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     grade = "A"
# elif marks >= 80:
#     grade = "B"
# elif marks >= 70:
#     grade = "C"
# elif marks >= 60:
#     grade = "D"
# else:
#     grade = "F"
# print(f"Your grade is: {grade}")



# # SIMPLE LOGIN SYSTEM
# set_your_username = str(input("Enter the username you want: "))
# set_your_password = str(input("Set your password: "))

# print("\033[1mDONE\033[0m")

# username = input("Enter your username: ")
# password = input("Enter your password: ")

# correct_admin = username == set_your_username
# correct_login = username == set_your_username and password == set_your_password
# if correct_admin or correct_login:
#     print("\033[1mAccess granted.\033[0m")
# else:
#     print("\033[1mAccess denied.\033[0m")



# # SIMPLE ATM SYSTEM
# set_pin = str(input("\033[1mSet your PIN: \033[0m"))
# put_balance = int(input("\033[1mPut your balance: \033[0m"))

# print("\033[1mDONE.\033[0m")

# pin = (input("\033[1mPIN: \033[0m"))
# if pin == set_pin:
#     print("\033[1mCORRECT PIN.\033[0m")
#     amount = int(input("\033[1mEnter withdrawal amount: \033[0m"))

#     if amount <= put_balance:
#         balance = put_balance - amount
#         print(f"\033[1mWITHDRAWAL SUCCESSFUL.\033[0m")
#         print(f"\033[1mREMAINING BALANCE: ${balance}\033[0m")
#     else:
#         print("\033[1mINSUFFIENT BALANCE.\033[0m")
# else:
#     print("\033[1mINCORRECT PIN.\033[0m")



# # DRIVING LICENSE ELIGIBILITY
# age = int(input("Enter your age: "))

# if age < 18:
#     print("You are underage. You cannot get a driving license.")

# elif age >= 18:
#     passed_test = input("Have you passed the driving test? (yes/no): ") == "yes"

#     if passed_test:
#         print("You can get a full driving license.")
#     else:
#         print("You are 18+, but you must pass the driving test first.")



#