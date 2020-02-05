pins=[]
User_status = True
while User_status:
    create_pin = int(input("Create a pin for your sim:"))
    create_pin_str= str(create_pin)
    if len(create_pin_str)<4:
        print("pin too short,use a minimum of four numbers")
    elif len(create_pin_str)>4:
        print("pin too long, use a maximum of four numbers")
    else:
        pins.append(create_pin_str)
        print("Pin successfully created, you can now login")
        User_status= False
else:
    start=1
    while start<=3:
        input_pin= input(
            "Enter your pin")
        if input_pin not in pins:
            print("wrong pin")
            attempt_left = 3 - start
            print("you have", attempt_left, " attempts left!")
            start += 1
            if attempt_left==0:
                print("SIM BLOCKED")
        else:
            print("login successful")
            break


