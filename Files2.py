# Task-2:
#     - Create a new file with name "rollNumbers.txt"
#       and insert 10 roll numbers into it.
#     - Within same file read and print only 4 roll 
#          numbers from it.
#     - Within the same file copy from 2nd to 6th roll
#         numbers into new file with name "specialStudents.txt"
#     - within the same file, print the content in specialStudents file
#     - within the same file, copy 1st, 3rd, 5th, 7th, 9th roll numbers into another file
#         with name "otherList.txt".
#     - read the content from otherList and print
 
# solution:
fileObj1 = open("rollNumbers.txt", "w")
fileObj1.write("10 \n 20 \n 30 \n 40 \n 50 \n 60 \n 70 \n 80 \n 90 \n 100 \n")
fileObj1.close()
 
fileObj1 = open("rollNumbers.txt", "r")
print(fileObj1.readline())
print(fileObj1.readline())
print(fileObj1.readline())
print(fileObj1.readline())
fileObj1.close()
 
fileObj1 = open("rollNumbers.txt", "r")
fileObj2 = open("specialStudents.txt", "w")
fileObj1.readline()
fileObj2.write(fileObj1.readline())
fileObj2.write(fileObj1.readline())
fileObj2.write(fileObj1.readline())
fileObj2.write(fileObj1.readline())
fileObj2.write(fileObj1.readline())
 
 
fileObj1.close()
fileObj2.close()
 
fileObj1 = open("specialStudents.txt", "r")
print(fileObj1.read())
fileObj1.close()
 
fileObj1 = open("rollNumbers.txt", "r")
fileObj2 = open("otherStudents.txt", "w")
fileObj2.write(fileObj1.readline())
fileObj1.readline()
 
fileObj2.write(fileObj1.readline())
fileObj1.readline()
 
fileObj2.write(fileObj1.readline())
fileObj1.readline()
 
fileObj2.write(fileObj1.readline())
fileObj1.readline()
 
fileObj2.write(fileObj1.readline())
fileObj1.close()
fileObj2.close()    
 
fileObj1 = open("otherStudents.txt", "r")
print(fileObj1.read())
fileObj1.close()
