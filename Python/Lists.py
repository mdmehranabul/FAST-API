"""
Lists are a collection of data
"""

my_list =[10,33,12,75,45,62]
print(my_list)

people_list = ["Eric", "Adolf","Jeff"]
print(people_list)

# people_list[0] = "Mac"
print(people_list[0])

print(people_list[0:2])

print(my_list[1:3])

my_list.append(100)
print(my_list)

my_list.insert(2,99)
print(my_list)

my_list.remove(45)
print(my_list)

my_list.pop(3)
print(my_list)



my_list.sort()
print(my_list)
