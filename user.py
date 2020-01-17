Maths= int(input("Enter your Maths Marks"))
if Maths >=0 and Maths<= 100:
    m=Maths
else:print("Invalid Marks")

English= int(input("Enter your English Marks"))
if English >=0 and English<= 100:
    e=English
else:print("Invalid Marks")

Kiswahili= int(input("Enter your Kiswahili Marks"))
if Kiswahili >=0 and Kiswahili<= 100:
    k=Kiswahili
else:print("Invalid Marks")

Science= int(input("Enter your Science Marks"))
if Science >=0 and Science<= 100:
    s=Science
else:print("Invalid Marks")

SST= int(input("Enter your SST Marks"))
if SST >= 0 and SST <= 100:
    st = SST
else:
    print("Invalid Marks")


total_marks= Maths+English+Kiswahili+Science+SST


Average = total_marks/5
if Average>=80 and Average<=100:
    print("Grade A")
elif Average>=70 and Average<=79:
    print("Grade B")
elif Average>=60 and Average<=69:
    print("Grade C")
elif Average>=50 and Average<=59:
    print("Grade D")
elif Average>=40 and Average<=49:
    print("Grade E")
elif Average >0 and Average<40:
    print("FAIL")
else:
    print("INVALID MARKS")
print("Maths:",Maths)
print("English:",English)
print("Kiswahili:",Kiswahili)
print("Science:",Science)
print("SST:",SST)
print("Total Marks:",total_marks)
print("Average:",Average)

