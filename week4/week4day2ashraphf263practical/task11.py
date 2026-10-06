def login(username, password):
    if username == "Ashraf Raeen" and password == "0327":
        return "Login Successful"
    else:
        return "Invalid Username or Password"


username = input("Enter Your Username: ")
password = input("Enter Your Password: ")

result = login(username, password)
print(result)
