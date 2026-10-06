def largest(a,b,c):
    if (a>b and a>c):
        return "a is the largest among all"
    elif (b>a and b>c):
        return "b is the largest among all"
    else:
        return "c is the largest among all"

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

largest = largest(a,b,c)
print (largest)