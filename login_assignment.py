username = "Mark"
email = "Mark@gmail.com"
password = "12345"

print("...Login to Facebook...")
login_user = input("Enter your username")


if login_user.capitalize() == username:
    login_mail = input("Enter your email account")
    if login_mail == email:
        login_password = input("Enter password:")
        if login_password == password:
            print("login successful")
        else:
            print("invalid password")
            print("re-enter password")
            login_password = input()
    else:
        print("invalid email")
        print("re-enter email")
        login_mail = input()

else:
    print("invalid username")
    print("re-enter username")
    login_user = input()





