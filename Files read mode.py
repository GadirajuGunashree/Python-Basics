# Task-1 (read mode)
 
# below line is responsible for opening a file in 'read' mode
fileObj = open("groups.txt", "r")
# below line alone is responsible to extract entire data
print(fileObj.read())
 
# below 3 lines are responsible to print output line by line
print(fileObj.readline())
print(fileObj.readline())
print(fileObj.readline())
 
# below 1 line is responsible to close the file
fileObj.close()
