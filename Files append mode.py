# Task-3 (append mode)
 
# below line is responsible for opening a file in 'append' mode
fileObj = open("groups.txt", "a")
# below line alone is responsible to insert entire data into the mentioned file at the end of existing data
fileObj.write("raj \n vamsi \n Akhila \n Harikha")
 
# below 1 line is responsible to close the file
fileObj.close()
