guess= int(input("guess a number"))
if guess%2 == 0:
    print("number divisible by 2")
elif guess%3 == 0:
    print("number divisible by 3")
elif guess%2 == 0 and guess%3 == 0:
    print("number divisible by 2 and 3")
else:
    print("number not divisible by 2 or 3")




user_A_input = int(input("Enter the first number"))
user_B_input = int(input("Enter the second number"))
if user_A_input > user_B_input:
    print(user_A_input,"is greater!")
else:
    print(user_B_input,"is greater!")