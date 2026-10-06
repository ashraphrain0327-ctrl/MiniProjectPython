def check_result(marks):
    if marks>=40:
        return "Pass"
    else:
        return "Fail"
marks=int(input("Enter Your Marks:"))
check = check_result(marks)
print ( check)