def is_adult(age):
    if age>=18:
        return "Adult"
    else:
        return "Minor"

age=int(input("Enter Your age:"))
print("you are", is_adult(age))
