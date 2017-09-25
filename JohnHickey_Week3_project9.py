


#Inputs
#file1 = input("what is the first file: ")
#file2 = input("what is the second file: ")

#Open the files and read the text and the line
#manual entry commented out for testing
#inputFile1 = open(file1, 'r')
#inputFile2 = open(file2, 'r')

#auto entry for testing
inputFile1 = open('1.txt', 'r')
inputFile2 = open('2.txt', 'r')

#read file
#text1 = inputFile1.read()
#text2 = inputFile2.read()
line1 = inputFile1.readline()
line2 = inputFile2.readline()

#print(text1)
#print("line1 =",line1)
#print("line2 =",line2)

#Set Counter
count = 1

#Loop to compare lines
while True:
    count +=1
    if line1 != line2:
        print("no")
        print(line1)
        print(line2)
        break
    line1 = inputFile1.readline()
    line2 = inputFile2.readline()
        
#    else:
#        print ("yes")
        

