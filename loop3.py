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
