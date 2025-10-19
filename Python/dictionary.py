"""
Dictionaries
"""

user_dictionary={
    'username':'mehran',
    'name':'mehran abul',
    'age':22,
}

print(user_dictionary)
print(user_dictionary.get('username'))

user_dictionary['married']=True
print(user_dictionary)
print(len(user_dictionary))

user_dictionary.pop('age')
print(user_dictionary)

# user_dictionary.clear()
print(user_dictionary)

# del user_dictionary

for x in user_dictionary:
    print(x)

for x,y in user_dictionary.items():
    print(x,y)


# Assignment

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for x,y in my_vehicle.items():
    print(x,y)

vehicle2=my_vehicle.copy()

vehicle2['number_of_tires']=4

vehicle2.pop('mileage')

for i in vehicle2:
    print(i)
