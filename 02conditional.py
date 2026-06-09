#ACTUAL TIME

import time
timestamp= time.strftime('%H:%M:%S')
print(timestamp)
hour=time.strftime('%H')
print(hour)
minute=time.strftime('%M')
print(minute)
second=time.strftime('%S')
print(second)

hour = int(hour)
if (hour >= 4 and hour <= 12):
    print("Good Morning.")
elif (hour > 12 and hour <= 18):
    print("Good Afternoon.")
else:
    print("Good Evening.")

#USER DEFINED TIME
import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("Enter the hour: "))
print (hour)

if(hour>=0 and hour<12):
    print("Good Morning")
elif(hour>=12 and hour<17):
    print("Good Afternoon")
elif(hour>=17 and hour<0):
    print("Good night")
else:
    print("Enter number between 0 and 24")