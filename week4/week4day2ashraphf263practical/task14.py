def calculate_total(a, b, c):
    return a + b + c
def calculate_average(total):
    return total / 3

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

total = calculate_total(a, b, c)
average = calculate_average(total)

print("Total:", total)
print("Average:", average)