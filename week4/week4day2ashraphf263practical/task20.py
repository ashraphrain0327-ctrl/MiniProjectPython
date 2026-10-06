def deposit(balance, amount):
    return balance + amount


def withdraw(balance, amount):
    if amount > balance:
        return "Insufficient Balance"
    return balance - amount


def check_balance(balance):
    return balance


balance = float(input("Enter initial balance: "))

operation = input("Enter operation (deposit/withdraw/check): ")

if operation == "deposit":
    amount = float(input("Enter deposit amount: "))
    balance = deposit(balance, amount)
    print("New balance:", balance)

elif operation == "withdraw":
    amount = float(input("Enter withdrawal amount: "))
    result = withdraw(balance, amount)
    print("Result:", result)

elif operation == "check":
    result = check_balance(balance)
    print("Current balance:", result)

else:
    print("Invalid operation")

