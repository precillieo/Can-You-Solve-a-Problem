def factorial(n):
    """
    This function returns the factorial of n.
    factorial(5) => 120
    """
    fact = 1
    if n == 0:
        return fact
    else:
        while n > 0:
            fact *= n
            n -= 1
        return fact

userno = int(input("Enter a number to get a factorial: "))
print(factorial(userno))

    
