#This program prints prime number between 1 to 100
import time



for i in range(2, 101):
   
    if (i%2) == 0:
        continue
    else:
        print(i)
        time.sleep(1)
    
