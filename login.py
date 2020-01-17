users = {}
passwords = {}
User_status = True


createLogin = input("Create login name: ")

if createLogin in users: # check if login name exists
    print ("User name already exist!")
else:
    createPassword = input("Create password: ")
    users[createLogin] = createPassword # add login and password
    print("Congratulations:", createLogin, "you have successfully created an account:")





username = input("Enter username:")
password = input("Enter password:")
while User_status:
    if username not in users:
        print("invalid username")

    elif username in users and users[username] == password:
        print ("login successful")
    else:
        print ("wrong password")

setPassword = str(input("Set Your Password"))
if len(setPassword)<5:
    print("Password too short")
elif len(setPassword)>15:
    print("Password too long")
else:
    print("Password successfully created")



store_user.append(user)
store_pass.append(password)