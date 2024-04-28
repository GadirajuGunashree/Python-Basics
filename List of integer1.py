# 1. Write a python program to accept list of integers
#     and print the total sum of odd elements within 
#     the list 
 
# solution:
nums = list(map(int, input().split()))
result = 0 
for ele in nums:
    if ele % 2 == 1:
        result = result + ele 
print(result)

# input
# 1 2 3 4 5 6 7 8 9 10
# output
# 25
