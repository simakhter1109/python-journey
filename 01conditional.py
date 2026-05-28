a = int(input("Enter a number: "))
if (a<0):
    print("The number is a negative number.")
elif(a>0):
     if(a<=20):
        print("The number is in between 1-20.")
     elif(a>=21 and a<=50):
        print("The number is in between 21-50.")
     else:
        print("The number is greater then 50.")
else:
    print("The number is 0.")           