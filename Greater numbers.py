def greaterNumbers(numbers):
    result=0
    n=len(numbers)
    for index in range(n):
        if numbers[index]>result:
            result = numbers[index]
    return result

numbers=[12,34,21,-12,34,55,56,34,12]
result=greaterNumbers(numbers)
print("Greater number is:",result)

# Output
# Greater number is: 56
