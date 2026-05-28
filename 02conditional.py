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