
def fact(num):
    if (num == 0 | num == 1):
        return 1
    else:
        return num*fact(num-1)



num = int(input('Enter any posititve number : '))
x =fact(num)
print('Factorial of the entered  number is : ',x)