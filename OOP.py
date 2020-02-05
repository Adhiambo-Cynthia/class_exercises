class Car:
            #all classes create objects and all objects contain attributes which aer intialized by _init_()
    make="Toyota"   #instance attributes are specific to each object but class attributes are same for all

car1=Car()
print(car1.make)

class Laptop:
    make="HP"
    '''def switch_on(self):   #switch on
        print("------LOADING!------")
    def switch_off(self):
        print("Shutting Down")'''
    def __init__(self,ram,hdd,screen):
        self.ram=ram
        self.hdd=hdd
        self.screen=screen

Elitebook=Laptop("150GB","1TB","16inch")
print(Elitebook.__dict__)



Elitebook=Laptop()
Elitebook.Ram="150GB"
Elitebook.HDD="1TB"
Elitebook.Screen="16inch"

Pavillion=Laptop()
Pavillion.Ram="100GB"
Pavillion.HDD="500GB"
Pavillion.Screen="12inch"
Elitebook.switch_on()
Elitebook.switch_off()
print(Elitebook)


class Person:
    def __init__(self,name,age,kgs):   #a constractor -an instance that calls itself
                                        #The task of constructors is to initialize(assign values)
        self.theName=name                #to the data members of the class when an object of class is created
        self.theAge=age
        self.theWeight=kgs
    def updateAge(self,newAge):
        self.theAge=newAge

Cynthia=Person("Cynthia",12,50)
print(Cynthia.__dict__)
Cynthia.updateAge(36)
print(Cynthia.theAge)
print(Cynthia.__dict__)
   #CONSTRACTOR 2
class Addition:
    def __init__(self,f,s):
        self.firstNO=f
        self.SecondNO=s
    def calculate(self):
        self.total= self.firstNO+self.SecondNO
        print("Addition of the numbers results",self.total)
object=Addition(34,800)
print(object.calculate())
   #Assignment
class Dog:
    def __init__(self,name,age):   #initialize the attributes
        self.name=name
        self.age=age

     #instatiate
dog1=Dog("tom",5)
dog2=Dog("eva",6)
dog3=Dog("terence",9)
def biggest_age(*args):
       result=max(args)
       return result
print(biggest_age(dog1.age,dog3.age,dog2.age))

