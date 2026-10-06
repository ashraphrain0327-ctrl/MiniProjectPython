def student_result(marks):
    if marks>=80:
        return "A " "Pass"
    elif marks>=70 and marks<=79:
        return "B " "Pass"
    elif marks>=60 and marks<=69:
        return "C " "Pass"
    elif marks>=50 and marks<=59:
        return "D " "Pass"
    elif marks<50 and marks>40:
        return "F " "Pass"
    elif marks>=40:
        return "Pass"
    else:
        return "Fail"

marks=int(input("Enter Your Marks: "))
result= student_result(marks)
print(result)