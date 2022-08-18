# Set is a collection of unordered but item can be added & removed, unindexed,unchangeable object
# Sets are written with curly brackets
# set repesents a group of unique elements.duplicate element can't be stored.
# set can store the same and different types of elements or objects
# set datatype does not support indexing, slicing

# Initilaze empty set
# x={} #wrong
# x= set()
s = {10, 40,67}
t = {10, 5.7,8}

# symmetric_difference_update finds the symmetric difference of two sets(non similar item) and update to the set thats calls the method.

t.symmetric_difference_update(s)
# print(t)

# Intersection() method returns a new set with elements that are common to all sets
s.intersection(t)
# s.intersection_update(t)
# print(s)

# s.discard(30)
# s.remove(1000)
# print(s)
# s.add(500)
# s.add(2287)
#s.update([774, 380, 180])

#print(s)


#Frozenset()
'''Frozenset method indicates that a python set has been frozen. This means the elements of a set which is frozen can't be changed. They are immutable.
A frozenset is essentially the unchangeable or immutable version of the set object.
'''

# class frozenset([iterable])
Grocery_item = {"Onion": 40, "Egg": 10, "Carrot": 50, "Rice": 70, "Apple": 240, "Sugar": 270, "Pulse": 370}
fset=frozenset(Grocery_item.items())
# Grocery_item["Onion"]=440
print(fset)