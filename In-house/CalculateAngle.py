# Write a program to print the angle between the hour and minute hands from given values.

#take the input
hour = int(input("Enter the hour: "))
minute = int(input("Enter the minute: "))

#calculate the angle between the hour and minute hand
hour_angle = (hour * 30) + (minute * 0.5)
minute_angle = (minute * 6)

#concatenate hour and minute to show time
time = str(hour) + ":" + str(minute)

#print the output
print("At time", time, "the angle between the hour and minute hand is", abs(hour_angle - minute_angle), "degrees.")
