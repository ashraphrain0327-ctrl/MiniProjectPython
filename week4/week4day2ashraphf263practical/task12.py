def calculate_bill(units):
    if units>1 and units<=20:
        return units*5
    elif units>20 and units<=30:
        return (20*5)+(units-20)*7
    elif units>=50:
        return (20*5)+(30*7)+(units-50)*7
    else:
        return "Ivalid"

units=int(input("Enter Units: "))
Totalbill= calculate_bill(units)
print(Totalbill)