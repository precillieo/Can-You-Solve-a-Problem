#python code

#list of numbers
list=[1,3,14,5,19,66,2,53,105,10,24,27,6,5,85,34,56,3,2,35,78,2,3,98,43,2,1,56,8,43,22,12]

print("\n \nThe list of numbers to be fitered through:\n" + str(list) + "\n\n")


#get the user tp input minimum value
specifiedNumber = int(input("Please specify a minimum number: "))

#create a new list to store all new values greater than the specified number
filteredList=[]


#run a for loop to get all numbers greater than the specified number
for x in list:
	if x > specifiedNumber:
		filteredList.append(x)

#print the numbers
print ("The numbers greater than \"" + str(specifiedNumber) + "\" are: " + str(filteredList))
