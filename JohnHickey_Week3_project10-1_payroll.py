"""
Program: payroll.py
Author: John Hickey

objective:
create a program that inputs a file from the user with payroll info
the file should contain the following on each line:
<last name> <hourly wage> <hours worked>
The program should return the followng on each line of output:
<last name> <hours worked> <wages paid>

input:
file name from the user

data analysis:
open the file and strip the strings to remove newlines
split the lines to create seperate strings for each entry on the line
Create variables for name, wages, hours from the string values
convert wages and hours from str to int

calculations:
wagesPaid = wages * hours

output:
print the header: "name" "hours" "wages paid"
print the values for each employee.

"""

#request file
file = input("enter the payroll filename: ")


#open the file
data = open(file, 'r')
#data = open('payroll.txt', 'r') #auto entry for testing

#print the header
print(" ") #add a space
print("%15s%15s%15s" % \
        ("Name", "Hours Worked", "Wages Paid"))

#loop for data analysis, calculations and output
for line in data:
      entries = line.strip()
      #print(entries)
      name,wages,hours = entries.split()
      wages = int(wages)
      hours = int(hours)
      wagesPaid = wages * hours             #calculate wages paid
      print("%15s%15d%15d" % \
            (name,wages,wagesPaid))
            
      




