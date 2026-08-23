# USER-DEFINED FUNCTION TO FIND GMEAN

def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
 
a=9
b=8
# gmean1 = (a*b)/(a+b)
# print(gmean1)  INSTEAD OF WRITING LIKE THIS
# USE
calculateGmean(a,b)

c = 8
d = 7
calculateGmean(c,d)

 
# AVERAGE

def average(a,b):
    print("The average is: ", (a+b)/2)

average(4, 6)