# A Python program to find the Least Common Multiple (LCM) of two positive integers.

def calculate_lcm(x, y):  
    # selecting the greater number  
    if x > y:  
        greater = x  
    else:  
        greater = y  
    while(True):  
        if((greater % x == 0) and (greater % y == 0)):  
            lcm = greater  
            break  
        greater += 1  
    return lcm    
  
# taking input 
n1 = int(input("Enter first positive integer: "))  
n2 = int(input("Enter second positive integer: "))  
print("The L.C.M. of", n1,"and", n2,"is", calculate_lcm(n1, n2))  