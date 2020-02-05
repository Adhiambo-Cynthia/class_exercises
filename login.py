#users = { "user_1":{"name":"cynthia", "password":"1234"},
          #"user_2":{"name":"tom","password": "6789"}
          #}
users=["cynthia"]
passwords=["1234"]

User_status = True

while User_status:
    createLogin = input("Create login name: ")

    if createLogin in users:  # check if login name exists
        print("User name already exist!")
        User_status = True
          #chucks you completely from the loop
    else:
        createPassword = input("Create password: ")
        if len(createPassword) < 5:
            print("Password too short! Kindly use a minimum of 5 chracters")
        elif len(createPassword) > 15:
            print("Password too long! Kindly use a maximum of 15 chracters ")
        else:
            print("Password successfully created,you can now login")
            users.append(createLogin)
            passwords.append(createPassword)
            User_status= False    #breaks te loop,takes you to the else part

        #users[createLogin] = createPassword  # add login and password

else:
    start=1
    while start<=5:
        username = input("Enter username:")
        password_put = input("Enter password:")
        if username not in users:
            print("invalid username")

        elif username in users and password_put not in passwords:
            print("wrong password")
            attempt_left = 5 - start
            print("you have", attempt_left, " attempts left!")
            start += 1
        else:
            print("login successful")
            break








