def greaterThan():
    """
    greaterThan() find all the values in a list are greater than a specified number.
    

    Variables: listNum: list; num: int

    """
    # variable to hold the list and the specified number
    listNum = [2,5,6,8,9,13,16,21,23,25,35,43,55,62,68,79]
    num = int(input("Enter a num: "))

    # checking if the number specified is greater than the list or not

    check = all(num >= i for i in listNum)
    print(check)

    # if statement to output the right message

    if check == True:
        print(f"{num} is greater than the list")
    else:
        print(f"{num} is not greater than the list")
    

  
    
    
    


greaterThan()
