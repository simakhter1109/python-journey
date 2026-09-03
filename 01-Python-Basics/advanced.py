# # PROBLEM 1
# students = {
#     "Alice": [85, 90, 78, 92],
#     "Bob": [72, 68, 75, 70],
#     "Charlie": [95, 88, 91, 97],
#     "David": [60, 65, 58, 62]
# }

# for name, marks in students.items():

#     average = sum(marks) / len(marks)

#     if average >= 90:
#         grade = "A"
#     elif average >= 80:
#         grade = "B"
#     elif average >= 70:
#         grade = "C"
#     elif average >= 60:
#         grade = "D"
#     else:
#         grade = "F"

#     print(f"{name}:")
#     print(f"  Marks: {marks}")
#     print(f"  Average: {average:.2f}")
#     print(f"  Grade: {grade}")
#     print()


# # PROBLEM 2
# numbers = [12, 45, 7, 89, 34, 67, 23]

# largest = numbers[0]
# second_largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num

# print("Largest:", largest)
# print("Second Largest:", second_largest)



# PROBLEM 3
password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True

if len(password) >= 8 and has_upper and has_lower and has_digit:
    print("Strong password")
else:
    print("Weak password")