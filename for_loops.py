numbers = [1, 2, 3, 4, 5]
for each_item in numbers:    # iterate over a sequence
    if each_item%2==0:
        print(each_item,"is even")
    else:
        print(each_item, "is odd")
else:
    print("last item reached")

for i in range(1,101):
    if i%3==0 and i%5==0:
        print("fizzBuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)




