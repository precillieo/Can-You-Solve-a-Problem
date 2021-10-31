
def compute(poly, n, x):
  
   
    result = poly[0]
  

    for i in range(1, n):
  
        result = result*x + poly[i]
  
    return result
  

  
poly = [3, -4, 3, -1]
x = 3
n = len(poly)
  
print("Value of polynomial is:", compute(poly, n, x))
