num1=int(input())
num2=int(input())
op=input()[0]
if op=='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=='/':
    print(num1//num2)
else:
    print("Invalid operator")
