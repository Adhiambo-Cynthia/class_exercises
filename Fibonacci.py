
my_list = []
x,y=0,1
z=x+y
my_list.append(x)
my_list.append(y)

while z<50:
    z=x+y
    my_list.append(z)
    x = y
    y = z


print(my_list)

