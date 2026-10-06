def calculator(a,b, operator):
    if (operator =='+'):
        return a+b
    elif(operator=='-'):
        return a-b
    elif(operator=='*'):
        return a*b
    elif(operator=='/'):
        return a/b
    else:
        return "Invalid"

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
operator=input("Enter Operator:")

calculator= calculator(a,b, operator)
print(calculator)
