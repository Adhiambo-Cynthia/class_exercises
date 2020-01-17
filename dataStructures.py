"""
data structure is a way of managing data in memory
in python: 1.list
           2.tuple
           3.dictionary
"""
# creating a list in python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] # lists are mutable
my_bool = [True, True, False, True, False]
list_of_lists = [[1, 2,3,4], [10, 10, True, [False, 9]], [10.5] ]
# list indexing
print(my_list[6])
print(my_list[::-1])
print(my_list[::-2])
print(my_list[::2])
print(my_list[1::2])   # start from position one, then skips one one afterwards
print(my_list[1::3])    #''''''''''', but skips two two afterwards
print(my_list[2::2])   # start from position two, then skips one one afterwards
print(my_list[1:-3:2])   #*****
print(my_list[-2::-1])    #will take from 8 and do the reverse
print(list_of_lists [1][3][0])


print(type(my_list))
"""tuple use ()
tuple is immutable
"""
days_of_week = ("mon", "tue", "wed", "thu", "fri", "sat", "sun",)

