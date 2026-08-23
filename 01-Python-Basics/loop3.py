# Print the elements of the given lisy using for loop.
num = [1, 4, 9, 16, 25, 36, 47, 64, 81, 100]

for el in num:
    print(el)

# Search for a number x in the given tuple using for loop.
num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 25, 36, 49, 64, 81, 100)
x = 49

idx = 0
for el in num:
    if(el == x):
        print(x, "found at index ", idx)
        break
    idx +=1

# Print numbers from 1 to 100.

for i in range (1, 101):
    print(i)

# Print numbers from 100 to 1.

for i in range (101, 0, -1):
    print (i)

# Print the multiplication table of number n.
 
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "X", i, "=", n * i)

# To find the suun of first n numbers using while loop.

# To find the factorial of first n numbers using for loop.