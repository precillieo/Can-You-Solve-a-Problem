def fizzbuzz(n):
    """
    This function prints integer 1 to N(N included), but print
    'Fizz' if an integer is divisible by 3,
    'Buzz' if an integer is divisible by 5 and
    'FizzBuzz' if an integer is divisible by both 3 and 5
    """
    for no in range(1,n+1):
        if no % 3 == 0 and no % 5 == 0:
            print("FizzBuzz")
        elif no % 3 == 0:
            print("Fizz")
        elif no % 5 == 0:
            print("Buzz")
        else:
            print(no)
    
