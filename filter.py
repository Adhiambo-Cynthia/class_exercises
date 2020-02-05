'''
filter(function_object, iterable)
function_object returns a boolean value and is called for each element of the iterable.
 Filter returns only those elements for which the function_object returns true.
'''
a = [1, 2, 3, 4, 5, 6]
result=filter(lambda x : x % 2 == 0, a) # Output: [2, 4, 6]
print(list(result))

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

result=filter(lambda x : x['name'] == 'python', dict_a) # Output: [{'name': 'python', 'points': 10}]
print(list(result))