from getpass import getpass

username = raw_input("What is your username ")
passw = getpass("Set your password ")

if passw == "dev123":
    print("Login Succsess! \n Welcome, "+ username +"!")
else:
    print("Incorrect password")