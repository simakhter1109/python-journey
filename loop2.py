# Print numbers from 1 to 100 using while loop.
i = 1
while (i <=100):
    print (i)
    i +=1

# Print the numbers from 100 to 1 using while loop.
i = 100
while (i >= 1):
    print (i)
    i -=1

# Print the multiplication table of a nummber n.
i = 1
while (i <= 10):
    print (5*i)
    i += 1
    
#Print the elements of the list given using while loop.
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
heroes= ["Ironman", "Captain America", "Thor", "Superman"]

idx = 0
while idx < len(heroes):
    print(heroes [idx])
    idx += 1

i = 0
while (i < len(nums)):
    print(nums[i])
    i += 1

# Search for a number x in the tuple given using while loop.
# First format.
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 25
i = 0 #initialization
while i < len(nums):
 if(nums[i] == x):
  print(x, "Found at idex ", i)
 i +=1

# My Format
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 26, 36, 34, 22)
x = 36
i = 0 #initialization
while i < len(nums):
 if(nums[i] == x):
  print(x, "Found at idex ", i)
 else:
  print("searcing...")
 i +=1