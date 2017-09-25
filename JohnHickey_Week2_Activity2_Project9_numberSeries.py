"""
Program: numberSeries.py
Author: John Hickey

Write a program that receives a series of numbers from the user
Once the user presses enter with no number the program calculates
the sum and average of all the numbers entered.

1. Initial values
       sum = 0.0
       count = 0
    
2. The inputs are
       data = the numbers inputted from the user
       
3. Computations:
       count = the total number of values entered
       number = data converted to float
       sum = the value of the initial sum + all subsequent values entered
           using a while loop
       average = sum / count
       
4. The outputs are
       the sum and the average
"""

# Initialize the constants
sum = 0.0
count = 0
               
# Request the inputs
data = input("Enter a number or press enter to finish: ")
 
# while loop
while data != "":
    number = float(data)
    sum += number
    data = input("Enter a number or press enter to finish: ")
    count += 1

# Display the sum and average of all numbers
if count == 0:  #to avoid dividing by zero for average
    print("you have to enter at least one number, please try again")
else:
    print("The sum of all numbers is: ", sum)
    print ("The average of all numbers is: ", sum / count)

