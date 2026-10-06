def get_grade(marks):
    if marks>=80:
        return "A"
    elif marks>=60:
        return "B"
    elif marks>=40:
        return "C"
    else:
        return "Fail"


marks=int(input("Enter Your marks:"))
print("Your Grade is", get_grade(marks))