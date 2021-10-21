# Python3 code to calculate age in years
from datetime import date

def calculateAge(born):
	today = date.today()
	try:
		birthday = born.replace(year = today.year)

	# raised when birth date is February 29
	# and the current year is not a leap year
	except ValueError:
		birthday = born.replace(year = today.year,
				month = born.month + 1, day = 1)

	if birthday > today:
		return today.year - born.year - 1
	else:
		return today.year - born.year
		
# Driver code
# Please make changes as below according to your birthday!!! as (YYYY,MM,DD).
print(calculateAge(date(2000, 8, 27)), "years")
