#Python Math library

#1 Write a Python program to convert degree to radian.
import math
x = math.pi
degree = float(input("Input degree: "))
print("Output radian:", round((degree*x)/180, 6))
print("")
#or just
print(math.radians(degree))
print("")

#2 Write a Python program to calculate the area of a trapezoid.
h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))
S = float(h*(a + b)/2)
print(S)
print("")

#3 Write a Python program to calculate the area of regular polygon.
n = int(input("# of sides: "))
l = float(input("length of a side: "))
S = n * pow(l, 2) / 4 / math.tan(math.pi/n)
print("Area = ", round(S, 2))
print("")

#4 Write a Python program to calculate the area of a parallelogram.
import math
a = float(input("base: "))
h = float(input("height"))
S = math.prod([a, h]) #можно заменить на умножение, но раз надо использлвать math....
print(S)