import random

random_num = random.randint(1,21)

start=1
while start<=3:
    guess= int(input("guess a number"))
    if guess != random_num:
        if (guess-random_num) < 3:
            print("wrong guess,try again,you're almost there")
        elif guess-random_num > 3:
            print("wrong guess,value entered too lar5ge, try again")
        attempt_left = 3 - start
        print("you have", attempt_left, " attempts left!")
        start += 1
        if attempt_left==0:
            print("Sorry,the number I was thinking of is", random_num)

    else:
            print("congratulation!you guessed correct!")
            break


        #too small
        #too large
        #num of attempts left