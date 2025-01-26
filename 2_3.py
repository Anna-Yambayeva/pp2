'''Python Lists'''

#Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist)

#Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]

#What is the data type of a list? -string
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

'''
There are four collection data types in the Python programming language:

1.List is a collection which is ordered and changeable. Allows duplicate members.
2.Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3.Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4.Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''



'''Access List Items'''

#Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")



'''Change Item Value'''

#Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)



'''Append Items'''

#Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)



'''Remove List Items'''

#Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove the first occurrence of "banana":
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist

#Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)



'''Loop Through a List'''

#Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]



'''List Comprehension'''

#transform this
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#to this
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#using: newlist = [expression for item in iterable if condition == True]

#Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"]

#With no if statement:
newlist = [x for x in fruits]

#You can use the range() function to create an iterable:
newlist = [x for x in range(10)]

#Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]

#Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]

#Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]

#Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]



'''Sort Lists'''

#Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)



'''Copy Lists'''

#Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Make a copy of a list with the : operator:
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)



'''Join Lists'''

#Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)



'''List Methods'''
'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''