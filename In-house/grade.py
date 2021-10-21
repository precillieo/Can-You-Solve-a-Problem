def grade():
    """
     grade: This function returns grades of a student
     based on the mark entered by the student.
    Variables: mark: int; name: str; subject:str
    
    """
    # variables to hold necessary details
    name = input("Enter your name: ")
    subject = input("Enter the subject you want to check your grade: ")
    mark = eval(input(f"What is your mark in {subject}: "))

    #checking for condition

    if mark >100 or mark <0:
        print("Please check the correctness of your mark")
    elif mark <50:
       print(f"Sorry {name}, your score is {mark} and your grade is F")
    elif mark >50 and mark <60:
        print(f"{name}, your score in {subject} is {mark} and your grade is C")
    elif mark >60 and mark <70:
        print(f"{name}, your score in {subject} is {mark} and your grade is B")
    else:
        print(f"{name}, your grade in {subject} is A")
        if mark >100:
            print("Please check the correctness of your mark")
        
        

grade()

