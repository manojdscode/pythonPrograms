import time
  
 
def triangle(n): 
      
    # number of spaces 
    k = 2*n - 2
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
       
        for j in range(0, k): 
            print(end=" ") 
      
        # decrementing k after each loop 
        k = k - 1
      
         
        for j in range(0, i+1): 
          
            # printing stars 
            print("* ", end="") 
      
        # ending line after each row 
        print("\r")
        time.sleep(1) 
  
# Driver Code 
n = int(input('Enter any positive number : '))
triangle(n) 