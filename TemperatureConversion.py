#Temperature Conversion: Write a python program that converts temperature from one unit to another(celcius to farenheit).

#Celsius To Fahrenheit
c = float(input("Enter temperature in celsius: "))  

fahrenheit = (c * 9/5) + 32

print('%.4f Celsius is: %0.4f Fahrenheit' %(c, fahrenheit))

#Fahrenheit to Celsius

f = float(input("Enter temperature in fahrenheit: "))

celsius = (f - 32) * 5/9

print('%.4f Fahrenheit is: %0.4f Celsius' %(f, celsius))


#output
'''
Enter temperature in celsius: 20
20.0000 Celsius is: 68.0000 Fahrenheit
Enter temperature in fahrenheit: 100
100.0000 Fahrenheit is: 37.7778 Celsius'''
