"""
Program: dif.py
Author: John Hickey

Objective:
create a program that prompts the user for two files to compare by line.
If the files are not the same, the progream prints "no"
and identifies the lines that are not the same.
If the files are the same, the program prints "yes"

inputs:
the names of 2 files to compare from the user.

data analysis:
open file, readfile to input a line of text as a string
for each line in the two files, compare the strings
if they are differnt, print "no" then print the two lines and break the loop.
if they are the same, proceed to the next line.
once all lines have been compared, if they were all the same, print "yes"

outputs:
are the files the same "yes" or "no" and which lines are mismatched.

"""


#Requests files to compare from the user
file1 = input("what is the first file: ")
file2 = input("what is the second file: ")

#Open the files
inputFile1 = open(file1, 'r')
inputFile2 = open(file2, 'r')

#auto opening hardcoded to make testing easier.
#inputFile1 = open('dif compare1.txt', 'r')
#inputFile2 = open('dif compare2.txt', 'r')

#read lines from the files
line1 = inputFile1.readline()
line2 = inputFile2.readline()

#Set Counter for the Loop
count = 1

#Loop to identify the differnces in the two files
while line1 !='' or line2 !='':
    if line1 != line2:
        #Output the mismatch to the user
        print("no")
        print(line1)
        print(line2)
        break
    line1 = inputFile1.readline()
    line2 = inputFile2.readline()
    count += 1

#Output that the script has completed and all lines were the same in both files
if line1 =='' and line2 =='':
    print ("yes")

        

