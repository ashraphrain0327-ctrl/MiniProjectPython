def number_category(number):
    if (number>0 and number%2==0):
        return "Positive Even"
    elif (number>0 and number%2 !=0):
        return "Postivie Odd"
    elif (number<0 and number%2 ==0):
        return "Negative Even"
    elif (number<0 and number%2 !=0):
        return "Negative Odd"
    else:
        return "zero"

number=int(input("Enter Number:"))
category= number_category(number)
print(category)