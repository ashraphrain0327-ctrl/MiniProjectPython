correct_username = "ashrafrain"
correct_password = "ashraf0327"

username = input("Enter your username: ").lower()
password = input("Enter your password: ").lower()
status = input("Enter account status: ")

if username == correct_username and password == correct_password:
    if status.lower() == "active":
        print("Login Successful")
    else:
        print("Account is Inactive")
else:
    print("Invalid Username or Password")