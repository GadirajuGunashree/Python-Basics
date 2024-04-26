# pattern-13

n = int(input())
val = 10
for i in range(1, n + 1):
   for j in range(i):
       print(val, end = " ")
       val = val+10
   print()

#10
#20 30
#40 50 60
#70 80 90 100
#110 120 130 140 150
