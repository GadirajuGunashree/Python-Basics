# Task-2 (write mode)
 
# below line is responsible for opening a file in 'write' mode
fileObj = open("groups.txt", "w")
# below line alone is responsible to insert entire data into the mentioned file
fileObj.write("varun \n swathi \n kiran \n vaishnavi")
 
# below 1 line is responsible to close the file
fileObj.close()
