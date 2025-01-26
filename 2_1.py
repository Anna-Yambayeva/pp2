'''boolean values'''

#True\False check
print(10 > 9)
print(10 == 9)
print(10 < 9)

#True\False in if condition
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")



#Any value may be evaluated sa True (except empty containers & some other stuff)
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#non-printed examples of True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#non-printed examples of False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#object that is made from a class with a function that returns 0 or False is also boolean False 
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))



#boolean can be returned as a result of a function separately too
def myFunction() :
  return True

print(myFunction())
#and be used in 'if' condition as well
if myFunction():
  print("YES!")
else:
  print("NO!")

#and there are many python built-in functions that return booleans
x = 200
print(isinstance(x, int))