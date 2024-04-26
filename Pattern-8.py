# pattern-8

n = int(input())
stars = n
spaces = 0


for i in range(n):
   for space in range(spaces):
       print(" ", end = "")
      
   spaces += 1
  
   for star in range(stars):
       print("*", end = "")
   stars -= 1
  
   print()

#*****
 #****
  #***
   #**
    #*
