def calculate_discount(price, discount):
    return price-discount/100*price
price=int(input("Enter Price:"))
discount=int(input("Enter discount:"))
final= calculate_discount(price, discount)
print(final)