def leastNumbers(numbers):
    result=0
    n=len(numbers)
    for index in range(n):
        if numbers[index]<result:
            result = numbers[index]
    return result

numbers=[12,34,21,-12,34,55,56,34,12]
result=leastNumbers(numbers)
print("least number is:",result)

# Output
# least number is: -12
