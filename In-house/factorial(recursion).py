def factorial(n):
    """
    This function returns the factorial of n.
    factorial(6) => 120
    """
    #base case
    if n == 0:
        return 1
    #recursive case
    else:
        fact = n * factorial(n-1)
        return fact
