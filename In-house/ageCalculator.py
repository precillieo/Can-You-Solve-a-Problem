# importing datetime library to use it to return current year
from datetime import datetime


def ageCal():
    """
    Age Calculator: This function calculates age based on the year of birth
    entered by the user.

    Variables:
    year_of_birth - the year of birth of the year
    age - calculates the age of the user from the year
    present_year - picks the current year
    """
    year_of_birth = int(input("Enter your year of birth: "))
    #calling the present year
    present_year = datetime.now().year
    # calculating age of the user
    age = present_year - year_of_birth
    print(f"Your year of birth is {year_of_birth} and your age is {age}")

ageCal()
