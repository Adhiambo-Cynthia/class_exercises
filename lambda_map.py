'''
The general syntax of a lambda function is quite simple:
lambda argument_list: expression
'''
sum = lambda x, y : x + y
print(sum(3,4))
print(type(sum))   #returns that its a function
#this returns the same result as
def sum(x,y):
   return x + y
print(sum(3,4))
#so instead of always writing functions,use lambda
def multiplication(list1):
    for i in list1:
         return i*2

print(multiplication([2,4,5]))
'''
the advantage of the lambda operator can be seen when it is used in combination with the map() function.
map() is a function which takes two arguments
r = map(function, sequence of iterables)
'''
def multiply2(x):
    return x * 2

result=map(multiply2, [1, 2, 3, 4])  # Output [2, 4, 6, 8] #if we didnt use map,
print(list(result))                                  # we would have created a for loop for each

#Let’s see how we can write the above code using map and lambda.
result=map(lambda x : x*2, [1, 2, 3, 4]) #Output [2, 4, 6, 8]
     #the function    the iterables/parameters
print(list(result))

 #below,each dict of dict_a will be passed as a parameter to the lambda function.

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

result=map(lambda x: x['name'], dict_a)  # Output: ['python', 'java']
print(list(result))
result=map(lambda x: x['points'] * 10, dict_a)  # Output: [100, 80]
print(list(result))
result=map(lambda x: x['name'] == "python", dict_a)  # Output: [True, False]
print(list(result))

#Multiple Iterables to the Map Function
list_a = [1, 2, 3]
list_b = [10, 20, 30]

result=map(lambda x, y: x + y, list_a, list_b)  # Output: [11, 22, 33]
print(list(result))

