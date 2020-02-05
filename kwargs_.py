'''
used to pass a keyworded, variable-length argument list
A keyword argument is where you provide a name to the variable as you pass it into the function.
One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it.
**kwargs differs from *args in that you will need to assign keywords to the arguments
'''
def myFun(**kwargs):
    for key, value in kwargs.items():
      print("%s == %s" % (key, value))


myFun(first='Geeks', mid='for', last='Geeks') #theres no positional order in which the items are output as in a list

def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

print_values(my_name="Sammy", your_name="Casey")

#Using *args and **kwargs to call a function

def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)



