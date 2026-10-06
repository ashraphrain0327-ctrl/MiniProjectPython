balance = float(input("Enter your account balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

if withdrawal > 0:
    if withdrawal <= balance:
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance")
else:
    print("Invalid Amount")