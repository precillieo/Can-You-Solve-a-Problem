import cmath

def quadratic(a, b, c):
 d = (b**2) - (4*a*c)
 sol1 = (-b-cmath.sqrt(d))/(2*a)
 sol2 = (-b+cmath.sqrt(d))/(2*a)
 print('The solution are {0} and {1}'.format(sol1,sol2))

Quadratic(1,5,6)
