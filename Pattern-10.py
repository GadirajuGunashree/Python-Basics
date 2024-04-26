# pattern-10

def print_reverse_pyramid(n):
    for i in range(n,0,-1):
        print(" " * (n-i) + "*" * (2*i-1))
n=int(input())
print_reverse_pyramid(n)

#*********
 #*******
  #*****
   #***
    #*
