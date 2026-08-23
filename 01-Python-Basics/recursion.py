# PRINT NAME N TIMES

# def print_name(i, n):
#     if i > n:      # Base case
#         return

#     print("Sim")
#     print_name(i + 1, n)   # Recursive call

# # Input
# n = int(input("Enter n: "))
# print_name(1, n)

# PRINT LINEARLY FROM 1 TO N

# def print_num(i, n):
#     if i > n:      # Base case
#         return
    
#     print(i)
#     print_num(i + 1, n)   # Recursive call

# # Input
# n = int(input("Enter n: "))
# print_num(1, n)

# PRINT FROM N TO 1

# def print_num(i, n):
#     if i < 1:      # Base case
#         return
    
#     print(i)
#     print_num(i - 1, n)   # Recursive call

# # Input
# n = int(input("Enter n: "))
# print_num(n, n)

# PRINT LINEARLY FROM N TO 1 (USING BACKTRACKING)

# def print_num(i, n):
#     if i < 1:      # Base case
#         return

#     print_num(i - 1, n)   # Recursive call
#     print(i)                 # Print while backtracking

# # Input
# n = int(input("Enter n: "))
# print_num(n, n)

# PRINT FROM N TO 1 (USING BACKTRACKING)

# def print_num(i, n):
#     if i > n:      # Base case
#         return

#     print_num(i + 1, n)   # Recursive call
#     print(i)                 # Print while backtracking

# # Input
# n = int(input("Enter n: "))
# print_num(1, n)

# SUM OF N NUMBERS

# def sum_n(n):
#     if n == 0:      # Base case
#         return 0

#     return n + sum_n(n - 1)

# # Input
# n = int(input("Enter n: "))
# print(sum_n(n))

# FACTORIAL OF N

def factorial(n):
    if n == 0:
        return 1   # IF I TAKE RETURN 0 THEN THE WHOLE FUNCTIOIN WILL GET MULTIPLIED BY 0 
    return n * factorial(n-1)

# INPUT
n = int(input("Enter n: "))
print(factorial(n))