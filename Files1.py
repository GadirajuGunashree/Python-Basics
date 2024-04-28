# Task-1:
#     - Create a new file with name "names.txt" and 
#         insert any 4 names.
#     - Within same file read and print those names.
#     - Within same file copy those 4 names to
#         another file with name "newNames.txt"
#     - within same file print those 4 names from 
#         "newNames.txt"
 
# solution:
 
    fileObj1 = open("names.txt", "w")
    fileObj1.write("raj \n kiran \n vaishu \n Krishna")
    fileObj1.close()
 
    fileObj1 = open("names.txt", "r")
    print(fileObj1.read())
    fileObj1.close()
 
    fileObj1 = open("names.txt", "r")
    fileObj2 = open("newNames.txt", "w")
    fileObj2.write(fileObj1.read())
    fileObj1.close()
    fileObj2.close()
 
    fileObj1 = open("newNames.txt", "r")
    print(fileObj1.read())
