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