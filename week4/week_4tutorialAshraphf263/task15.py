def largest(a,b):
    if a>b:
        return "a"
    else:
        return "b"

a=int(input("Enter First Number:"))
b=int(input("Enter second Number:"))
print("Largest Number is", largest(a,b))