#function to calculate trig of input received
import math

info = """

What Trigonometry function would you like to carry out?
input 1 for sine (sin),
input 2 for cosine (cos),
input 3 for tangent (tan),
input 4 for cosecant (cosec),
input 5 for secant (sec),
input 6 for cotangent (cot).

input: """

type = int(input(info))
angle = int(input("Please input the angle (degree): "))

if type == 1:
	functionName = "sin"
	result = math.sin(math.radians(angle))
elif type == 2:
	functionName = "cos"
	result = math.cos(math.radians(angle))
elif type == 3:
	functionName = "tan"
	result = math.tan(math.radians(angle))
elif type == 4:
	functionName = "cosec"
	result = 1 / math.sin(math.radians(angle))
elif type == 5:
	functionName = "sec"
	result = 1 / math.cos(math.radians(angle))
elif type == 6:
	functionName = "cot"
	result = 1 / math.tan(math.radians(angle))

print("\nThe value of {0} {1} is {2}".format(functionName, str(angle), str(round(result, 3))))