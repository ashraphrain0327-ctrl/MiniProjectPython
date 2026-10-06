def shopping_bill(price, quantity, discount):
    total_price=quantity*price
    discount_amount=discount/100
    final_amount=total_price-discount_amount
    return final_amount
price=float(input("Enter Price: "))
quantity=int(input("Enter quantity: "))
discount=int(input("Enter Discount: "))

final_amount=shopping_bill(price, quantity, discount)

print("Final Amount is ", final_amount)
