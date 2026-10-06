def divisible_by_5(number):
    if number%5==0:
        return "Yes"
    else:
        return "No"

number = int(input("Enter Your Number:"))
divisible= divisible_by_5(number)
print(divisible)