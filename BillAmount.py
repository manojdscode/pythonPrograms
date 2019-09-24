
# This is a simple program to calcualte the electricity bill amount.


def BillAmount(name,units):
    if units <=200:
        print("Hi",name)
        print("Your electricity bill is NILL for this months ")
    elif units<=300:
        bill= (300-200)*4     #Electricity charge is Rs. 4 per units
        print("Hi",name)
        print("Your electricity bill is %f for this months ",bill)
    elif units<=400:
        bill= (400-200)*5     #Electricity charge is Rs. 5 per units
        print("Hi",name)
        print("Your electricity bill is %f for this months ",bill)
    elif units<=500:
        bill= (500-200)*6     #Electricity charge is Rs. 6 per units
        print("Hi",name)
        print("Your electricity bill is %f for this months ",bill)
    else:
        bill= (500-200)*6     #Electricity charge is Rs. 6 per units
        print("Hi",name)
        print("Your electricity bill is %f for this months ",bill)
        



    







#User input

name = input('Enter your name : ')
units = int(input('Enter how much electrticity units you consumed this month : '))

BillAmount(name,units)
