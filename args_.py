'''
*args allows you to do is take in more arguments than the number of formal arguments that you previously defined.
 With *args, any number of extra arguments can be tacked on to your current formal parameters
'''


# Python program to illustrate
# *args with first extra argument
def myFun(arg1, *args):
    print("First argument :", arg1)
    for arg in args:
        print("Next argument through *argv :", arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

