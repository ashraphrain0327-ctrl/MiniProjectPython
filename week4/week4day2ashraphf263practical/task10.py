def get_grade(marks):
    if marks>=80 and marks<=100:
        return "A"
    elif marks>=70 and marks<=79:
        return "B"
    elif marks>=60 and marks<=69:
        return "C"
    elif marks>=50 and marks<=59:
        return "D"
    else:
        return "F"

marks=int(input("Enter Your Marks:"))
grade= get_grade(marks)
print(grade)