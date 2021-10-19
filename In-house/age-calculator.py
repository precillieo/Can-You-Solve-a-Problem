#!/usr/bin/env python

from datetime import datetime


today = datetime.today() #current date

def ageCalc():
    '''
    ageCalc(birth date)
        Returns an integer corresponding to a person's age based on the current date an the birth date.

        Parameters: birth_date: str
    '''
    birth_date = input('Digit your birth date in this format (dd/mm/yyyy): \n')
    birth_date = datetime.strptime(birth_date, '%d/%m/%Y').date()  #convert  input in datetime object
    how_old = today.year - birth_date.year #calculating the age
    print('You are ',how_old,'years old')
    return 0

ageCalc()






