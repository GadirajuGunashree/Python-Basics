def numbersGraterThanTarget(listOfNumbers,target):
    result=0
    n=len(listOfNumbers)
    for index in range(n):
        if listOfNumbers[index]>target:
            result=result+1
    return result


listOfNumbers=[12,34,21,-12,34,55,56,34,12]
target=340

result= numbersGraterThanTarget(listOfNumbers,target)
print("total numbers greater than target are:",result)

# Output
# total numbers greater than target are: 0
