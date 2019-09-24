# This is simple program salary slip

def salary(name,gender,c_salary):
    if c_salary>10000:
        if gender =='M':
            new_salary = 1.05*c_salary
            print("Hi",name)
            print("Your new sallary is %f",new_salary)
        if gender =='F':
            new_salary = 1.1*c_salary
            print("Hi",name)
            print("Your new sallary is %f",new_salary)    
        else:
            print("Something went worng!!!")

    else:
        new_salary = 1.02*c_salary
        print("Hi",name)
        print("Your new sallary is %f",new_salary)





#User input
name=input('Enter your name : ')
gender = input('Enter yoru gender as M or F :')
c_salary=int(input('Enter your current salary : '))


#Diver
salary(name,gender,c_salary)