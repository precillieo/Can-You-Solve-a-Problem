#!/usr/bin/env python

from datetime import date
from datetime import datetime


today = date.today() #current date

def ageCalc(birth_date):
    '''
    ageCalc(birth date)
        Returns an integer corresponding to a person's age based on the current date an the birth date.

        Parameters: birth_date: str
                        String format: dd/mm/aa
    '''

    birth_date = datetime.strptime(birth_date, '%d/%m/%Y').date()
    how_old = today.year - birth_date.year
    print(how_old)
    return 0

ageCalc('08/06/1993')






