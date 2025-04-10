'''Python Classes'''
#1 Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.
class dialog:
    def __init__(self):
        self.name=" "
    def getString(self):
        print("What's your name? ")
        self.name=input()
    
    def printString(self):
        print(self.name.upper(),", nice to meet you!")

you= dialog()
you.getString()
you.printString()

#2 Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
class shape:
    def __init__(self):
        pass
    
    def area(self):
        print("Area:", 0)

class square(shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        print("Area:", self.length * self.length)

me=shape()
me.area()
he=square(5)
he.area()

#3 Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.
class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        print("Area:", self.length * self.width)

she=rectangle(5,2)
she.area()

#4 Write the definition of a Point class...
import math
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, ";", self.y)
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

p1 = point(3, 4)
p2 = point(6, 8)
p1.show() 
p2.show()  
print("Distance:", p1.dist(p2))  
p1.move(10, 12)
p1.show()  

#5 Create a bank account class that has attributes owner, balance and two methods deposit and withdraw.
class account: 
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw (self, amount):
        if (amount<=self.balance):
            self.balance-=amount
            print("Balance: ",self.balance)
        else:
            print("There is not enough money on the balance")

    def deposit (self, amount):
        self.balance+=amount
        print("Balance: ",self.balance)

a1=account("Lily",3000)
a1.withdraw(1000)
a1.deposit(100)
a1.withdraw(3000)

#6 Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.
def is_prime(x):
    if x<2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False
    return True

mylist=[1, 2, 3, 4, 5, 6, 7, 8, 9, 31]
print(list(filter(lambda x:is_prime(x),mylist)))