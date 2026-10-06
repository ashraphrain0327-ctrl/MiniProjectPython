def age_category(age):
    if age<13:
        return "child"
    elif age>13 and age<=19:
        return "Tennager"
    elif age>20 and age<=59:
        return "Adult"
    else:
        return "Senior Citizen"

age=int(input("Enter Your age:"))
age= age_category(age)
print(age)