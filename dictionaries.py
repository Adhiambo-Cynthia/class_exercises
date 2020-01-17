this_dict = {
    "name": "Cynthia",
    "interests": ["swimming", "dancing", "eating"],  # key must be unique,wrapped btwn """
    "age": 10,
    "workdays": ("mon", "tue", "wed"),
    "parents": {"mother": "sarah"}
}  # unordered collection of items
print(type(this_dict))
print(this_dict)
# retrieve name-use square brackets to pass the key
print(this_dict["name"])
cynthia_dict = {
    "name": "Cynthia",
    "schools": {
        "primary_1":{"sch_name": "Elgon_Academy",
                "population":{"boys": "300", "girls": "400"},
                "head teacher":{"first-name": "Eric", "second_name": "Lema"}},
        "primary_2":{"sch_name": "Simba_Academy",
                "population": {"boys": "900", "girls": "800"},
                "head teacher": {"first-name": "Mike", "second_name": "Ouma"}}
                },
    "languages": ["English", "Swahili"]

}
print(cynthia_dict)
print(cynthia_dict["schools"]["primary_1"]["head teacher"])
my_list = [1, 2, 3,4 ,5 ,6 ,7 ,8,9]
list_b =[]  # task 3; create a new list with 1st and last item
list_b.append(my_list[0])
list_b.append(my_list[-1])
print(list_b)     #orrr....
print(my_list[::8])   #take the first and jump 7 others

my_list2 =[1023, 43546, 67845, 54767]  # finding maximum
print(max(my_list2))
del my_list2[3]    # deleting an item in a list
print(my_list2)

x = (1, 2,3, 4, 5, 6, 7,8, 9,10)
print(x[0], x[1], x[2], x[3], x[4]) # print into two halves
print(x[5], x[6], x[7], x[8], x[9])

 # another method by converting first to a string
first_half = (x[0:5])
second_half =(x[6:9])
first_string = str(first_half)
second_string = str(second_half)
print(first_string.strip("()"))
print(second_string.strip("()"))
print(*x, sep=",")   # just removes the parenthesis



