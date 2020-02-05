"""def add3numbers(a, b, c):
    sum= a+b+c
    return sum  #to use for another operation
print(add3numbers(12,86,98))
x=add3numbers(12,86,98)
if x>100:
    print("<100")
else:
    print(">100")"""


def helloName(name):
    return "Hello {}!".format(name)
    # return f"Hello {name}"       #f'string
# orrr
#result =  "Hello " + name
#return result

print(helloName("Gerald"))

   #B
def Area(b,h):
    result= 0.5*b*h
    return result

print(Area(2,3))

 #C
def maxRange(x,y):
    result=(x+y)-1
    return result

print(maxRange(8,10))

   #D
def firstValue(list):
    result=list[0]
    return result

print(firstValue([56,78,45,98]))

   #E
def animals(chicken,pigs,cows):
    x=chicken*2
    y=pigs*4
    z=cows*4
    result= x+y+z
    return result
print(animals(2,3,5))

   #F
def largestNo(list):
    result=max(list)
    return result
print(largestNo([4,6,2,8]))

  #G
def difference(list):
    x=max(list)
    y=min(list)
    z=x-y
    return z
print(difference([10, 15, 20, 2, 6]))

  #H
def concat(list1,list2):
    list3=list1+list2
    return list3

print(concat([1,2,3],[5,6,7,8]))

  #I
def comp(string1,string2):
    x=len(string1)
    y=len(string2)
    if x==y:
        return True
    else:
        return False
print(comp("AB","CDE"))

mydict  = {
    'name' : 'cynthia',
    'age' : 30,
    'name2': 'misky',
    'age' :45              #looping of a dictionary
}

for key, value in mydict.items():
    print(key, value)

for key in mydict.keys():
    print(key)

   #J
def convert_to_array(dict):
    mylist = []
    for key, value in dict.items():
        mylist.append([key, value])
    return  mylist

print(convert_to_array({"a": 1, "b": 2 }))
print(convert_to_array({ "shrimp": 15, "tots": 12 }))
   #K
def profit(dict):
    profit1= (dict["sell"]-dict["cost"])*dict["inventory"]
    return round(profit1)
print(profit({
  "cost": 32.67,
  "sell": 45.00,
  "inventory": 1200}))

def calculate_score(list):
     count_list=[]
     for i in list:
        if i[0] == i[1]:
            count_list.append("Tie")
        if i[0]=="R":
            if i[1]=="P":
                       count_list.append("ben")
            elif i[1]=="S":
                    count_list.append("abigael")
        if i[0] == "P":
            if i[1]=="S":
                        count_list.append("ben")
            elif i[1]=="R":
                        count_list.append("abigael")
        if i[0] == "S":
            if i[1] =="R":
                     count_list.append("ben")
            elif i[1]=="P":
                        count_list.append("abigael")
     Abigael= count_list.count("abigael")
     Ben=count_list.count("ben")
     Draw=count_list.count("Tie")
     # print(count_list)

     if Abigael>Ben and Abigael>Draw:
         return("Abigael wins")
     elif Ben>Abigael and Ben>Draw:
         return("Ben wins")
     else:
         return("Draw")

print(calculate_score([["R", "P"], ["R", "S"], ["S", "P"]]))
print(calculate_score([["R", "R"], ["S", "S"]]))

user_input=input("enter")
if user_input=='YES' or user_input=='Yes' or user_input=='yes':
    print("Yes")
else:
    print("No")









