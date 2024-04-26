# pattern-12

n = int(input())
spaces = 0
for i in range(n, 0, -1):
   val = 1
   for space in range(spaces):
       print(" ", end = " ")
   spaces += 1
  
   for num in range(2 * i-1):
       print(val, end = " ")
       val += 1
   print()


#1 2 3 4 5 6 7 8 9 
  #1 2 3 4 5 6 7 
    #1 2 3 4 5 
      #1 2 3 
        #1 
