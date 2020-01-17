if 10+10 == 20:
    print("Cynthia")

marks = int(input("Enter your Marks"))
if marks>=80 and marks<=100:
    print("Grade A")
elif marks>=70 and marks<=79:
    print("Grade B")
elif marks>=60 and marks<=69:
    print("Grade C")
elif marks>=50 and marks<=59:
    print("Grade D")
elif marks>=40 and marks<=49:
    print("Grade E")
elif marks >0 and marks<40:
    print("FAIL")
else:
    print("INVALID MARKS")


x = (1, 2,3, 4, 5, 6, 7,8, 9,10)
x_string = str(x)
first_half = (x_string[:5])
print(first_half.strip("()"))


