print("hello world")

def solveIt2():
    print("this is FIRST line getting exicuted")
    print("this is line 123")

print("I am not getting PRINTED")

def solveIt4():
    print("i am solveIt4")
    print("this is getting exicuted")
    solveIt2()
    print("second line is getting exicuted")

def solveIt():
    print("this is line 111")
    print("this is line 112")
    solveIt4()
    print("solveIt4 haven't completed its execution")

def sumOfTwoNumbers(num1,num2):
    print("After execution")
    solveIt()
    print("Nothing gets printed")
    result = num1 + num2
    print("Before execution")
    return result

print("Last line is getting printed")
num1 =int(input())
num2 =int(input())
result=sumOfTwoNumbers(num1,num2)
print(result)
print("First line is getting executed")

# output
# hello world
# I am not getting PRINTED
# Last line is getting printed
# After execution
# this is line 111
# this is line 112
# i am solveIt4
# this is getting exicuted
# this is FIRST line getting exicuted
# this is line 123
# second line is getting exicuted
# solveIt4 haven't completed its execution
# Nothing gets printed
# Before execution
# 40
# First line is getting executed
