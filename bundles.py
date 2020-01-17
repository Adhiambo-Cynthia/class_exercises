account_balance = 500
user_pin = 12345

bundle_cash= int(input("how much would you like to use"))
if bundle_cash> 0 and bundle_cash <= account_balance:
    login_pin= int(input("Enter your pin"))
    if login_pin == user_pin:
        print("you have succesful been awarded airtime worth:", bundle_cash)
        new_balance = account_balance - bundle_cash
        print("your new balance is :", new_balance)
    else:
        print("invalid pin")


else:
    print("insufficient funds,your current account balance is:",account_balance)


