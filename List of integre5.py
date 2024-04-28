# [10:18 am, 28/4/2024] Homie🫂: 5. Write a python program to accept string and print 
#     total number of "ab" substring present in given string
 

 
# solution
word = input()
result = 0 
n = len(word)
# n = 8
 
for index in range(n - 1):
    if word[index] == 'a' and word[index + 1] == 'b':
        result += 1 
 
print(result)
# Input
# # freabsdabsdaab 
# Output
# # 3
# [10:40 am, 28/4/2024] Homie🫂: Output
# GT
# Wheels count is: 12
# One
# Two
# Brand name is: GT
# Wheels count is: 12
# One
# Two
# Sorry, I am not going to print speed
# Wheels count is: 12
# One
# Two
# Brand name is: Pulsar
# Wheels count is: 12
# One
# Two
