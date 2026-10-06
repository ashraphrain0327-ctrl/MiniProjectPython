def calculate_salary(basic_salary):
    if basic_salary<30000:
        return basic_salary*0.10+basic_salary
    elif basic_salary>=30000 and basic_salary<=50000:
        return basic_salary*0.15+basic_salary
    else:
        return basic_salary*0.20+basic_salary

basic_salary=int(input("Enter Your Basic Salary: "))
Final_Salary=calculate_salary(basic_salary)
print("Your Salary With allowence is ", Final_Salary)