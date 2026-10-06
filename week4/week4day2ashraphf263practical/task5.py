def smallest(a,b,c):
    if (a<b and a<c):
        return "a is the smallest among all"
    elif (b<a and b<c):
        return "b is the smallest among all"
    else:
        return "c is the smallest among all"

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

smallest = smallest(a,b,c)
print (smallest)