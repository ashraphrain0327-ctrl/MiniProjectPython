def calculate_result(m1, m2, m3):
    total= m1+m2+m3
    average = total/3
    return total, average

m1 = int(input("Enter M1:"))
m2 = int(input("Enter M2:"))
m3 = int(input("Enter M3:"))

total, average= calculate_result(m1, m2, m3)

print("Total", total)
print("Average", average)