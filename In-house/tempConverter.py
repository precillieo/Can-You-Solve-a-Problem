def tempConvert():
    """
    tempConvert() convert temperature from one unit to another,
    Celcius to Fahrenheit (°C to °F) and vice versa.

    Variables: unit: str; value: int

    """
    # take input from the user
    unit = input("Which unit is your temperature: C or F? ")
    value = eval(input("Enter the value of your temperature you want to convert: "))

    # converting user input to lower case
    unit = unit.lower()

    # condition to check the unit we want to onvert from for the right formular

    if unit == "c":
        
        # capturing the formular and rounding it to two decimal places
        Fahrenheit = round((value *(9/5)) + 32, 2)
        print(f" {value}°C  is {Fahrenheit}°F.")
        
    else:
        Celsius = round((value - 32) * (5/9), 2)
        print(f" {value}°F is {Celsius}°C.")
        
tempConvert()
