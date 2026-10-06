def calculate_bmi(weight, height):
    BMI=weight/(height*height)

    if BMI<18.5:
        return "Underweight"
    elif BMI>=18.5 and BMI<=24.9:
        return "Normal"
    elif BMI>=25 and BMI<=29.9:
        return "Overweight"
    else:
        return "Obese"

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

BMI=calculate_bmi(weight, height)
print("BMI Category: ", BMI)