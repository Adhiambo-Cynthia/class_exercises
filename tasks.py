taskList = [23, "Jane", ["Lesson 23", 560, {"currency" : "KES"}], 987, (76, "John")]
print(type(taskList))
print(taskList[2][2]["currency"])
print(taskList[2][1])
print(len(taskList))
taskList[3] = 789   #change 987 to 789
print(taskList)
# ORRR...
x = taskList[3]
y = str(x)   #convert it to a string
z= y[::-1]     # Reverse it
a = int(z)   #make it back to an integer
taskList[3] = a
print(taskList)

taskList[4]= (76, "Jane")
print(taskList)