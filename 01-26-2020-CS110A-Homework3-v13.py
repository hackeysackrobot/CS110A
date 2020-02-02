# CS110A
# Homework 3
# 01-26-2020

# Program divides the number of riders by the number of days.
# Then, program outputs the resulting average daily ridership.




x = str(input("Welcome to the Muni Ridership Calculator. Which Muni line did you survey? "))

y = int(input("How many days did you survey? "))

z = int(input("How many riders did you count? "))

print("Average riders per day " , x , z / y)
