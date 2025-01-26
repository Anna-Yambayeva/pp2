'''Python Sets'''

#Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Sets are unordered, so you cannot be sure in which order the items will appear.
#Once a set is created, you cannot change its items, but you can remove items and add new items.

#Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#he values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}

#What is the data type of a set? -string
myset = {"apple", "banana", "cherry"}
print(type(myset))

#Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)



'''Access Set Items'''

#Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#Check if "banana" is NOT present in the set:
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)



'''Add Set Items'''

#Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)



'''Remove Set Items'''

#Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}

del thisset

#print(thisset) will give error



'''Loop Sets'''

#Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)



'''Join Sets'''

#Join set1 and set2 into a new set:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

#Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

#Join a set with a tuple:
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

#The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Join set1 and set2, but keep only the duplicates:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#Use & to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

#Keep the items that exist in both set1, and set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

#Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

#Keep all items from set1 that are not in set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

#Use - to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

#Use the difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

#Keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

#Use ^ to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

#Use the symmetric_difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

'''Set Methods'''
'''
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update() 	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()      Returns a set, that is the intersection of two other sets
intersection_update()       Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()      Returns whether another set contains this set or not
<	Returns whether all items in this set is present in other, specified set(s)
issuperset()        Returns whether this set contains another set or not
>	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()      Returns a set with the symmetric differences of two sets
symmetric_difference_update()       Inserts the symmetric differences from this set and another
union()     Return a set containing the union of sets
update()        Update the set with the union of this set and others
'''
