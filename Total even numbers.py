def totalEvenNumbers(listOfNumbers,target):
    result=0
    n=len(listOfNumbers)
    for index in range(n):
        if listOfNumbers[index]%2==0:
            result=result+1
    return result


listOfNumbers=[12,34,21,-12,34,55,56,34,12]
target=340

result= totalEvenNumbers(listOfNumbers,target)
print("total numbers even numbers are:",result)

Output
total numbers even numbers are: 7
