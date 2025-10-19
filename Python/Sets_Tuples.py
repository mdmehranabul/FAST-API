"""
Sets are similar to lists but are unordered and do not contains duplicates.
"""

my_set = {1,2,3,4,5,1,2,3}
print(my_set)
print(len(my_set))

# print(my_set[0]) # Error - Index not allowed for sets

my_set.discard(5)
print(my_set)

my_set.add(12)
print(my_set)

# my_set.clear()
print(my_set)

my_set.update({7,8,9})
print(my_set)

"""Tuple - 
Ordered like lists but unchangeable"""

my_tuple=(1,2,3,4,5)
print(my_tuple)

print(len(my_tuple))
print(my_tuple[2])

# my_tuple[2]=54 # Error - Tuple does not support assignment



### LIST ASSIGNMENT

zoo= ["Lion", "Tiger", "Zebra", "Giraffe", "Crocodile"]
zoo.pop(3)
print(zoo)

zoo.append("Deer")
print(zoo)

zoo.pop(0)
print(zoo)

print(zoo[0:3])