def withdraw(balance, amount):
    if amount<=0:
        return "Invalid Amount"
    elif amount>balance:
        return "Insufficient Balance"
    else:
        return balance-amount

balance=float(input("Enter Balance: "))
amount=float(input("Enter Your Amount: "))

withdraw=withdraw(balance, amount)

print(withdraw, "Successful Transaction")