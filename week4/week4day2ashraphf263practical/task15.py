def calculate_total(Python_Marks, Web_Marks, Database_Marks):
    return Python_Marks+Web_Marks+Database_Marks

def average(total):
    return total/3

def grade(average):
    if average>=80:
        return "A"
    elif average>=70:
        return "B"
    elif average>=60:
        return "C"
    elif average>=50:
        return "D"
    elif average>=40:
        return "E"
    else:
        return "Fail"

def check_pass_fail(average):
    if average>=40:
        return "Pass"
    else:
        return "Fail"

Student_Name=input("Enter Student Name: ")
Python_Marks= float(input("Enter Python Marks: "))
Web_Marks= float(input("Enter Web Marks: "))
Database_Marks= float(input("Enter Database Marks: "))

total = calculate_total(Python_Marks, Web_Marks, Database_Marks)
average = average(total)
grade = grade(average)
result = check_pass_fail(average)


print("Student Name: ", Student_Name)
print("Total: ", total)
print("Average: ", average)
print("Grade: ", grade)
print("Result: ", result)