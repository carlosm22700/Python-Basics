# ========== General Purpose Containers ========== #
'''
ways for application to maintain collections of data.

in JS we use Arrays and Objects

Python has Dictionaries, Lists, Tuples
'''

# ========== Dictionaries ========== #

'''
Dictionaries are to python as objects are to JS.

A dictionary provides a container for key: value pairs.

In python these are items vs properties

Dictionaries have a class type of dict
'''
# Basic syntax

student = {
    'name': 'Carlos',
    'course': 'SEI',
    'Current Week': 7
}

'''
Dictionaries are mutable:

-Values assigned to a key can be changed
-Additional items can be added
-Existing items can be deleted
'''

# any immutable type can be used as a key, including numbers and types

option = 3

d = {
    option: 'Three'
}

'''
The above dict, has 1 item with a key of 3 that holds the value of three. The value of option is 'copied' as a key, no link to the option var is created. 
'''

# Square Bracket notation to get and set item's value:

name = student['name']
print(name)
# => Carlos
student['name'] = 'Martinez'
print(student['name'])
# => Martinez

# WE CANNOT ACCESS ITEMS IN DICT USING DOT NOTATION

# get() method

'''
when accessing a key that does not exist in a dictionary, a KeyError is thrown

we can avoid this by using the get() method
'''

skills = student['skills']
# => KeyError: 'skills'
print(student.get('skills'))
# => None
# Provide a default value if key not in dict
print(student.get('skills', {'HTML': 5, 'JAVASCRIPT': 4}))
# => {'HTML': 5, 'JAVASCRIPT': 4}

# the in operator

'''
we can avoid KeyErrors by using the in operator to check if the dict includes a certain key
'''

if 'course' in student:
    print(f"{student['name']} is enrolled in {student['course']}")
else:
    print(f"{student['name']} is not enrolled in a course")

# The in operator always returns a boolean


# Adding items
'''
simply assigning to a key that does not exist will create a new item in the dictionary.
'''

student['age'] = 22

# if an age item already exists, it will be updated

# Deleting Items
'''
The del statement is used to delete an item from a dictionary
'''

del student['age']
# verify the item was deleted; delete statements do not return a value 👀
'age' in student
# => false

# Number of Items
'''
we use built in len() function to retrieve the number of items in a dict.
'''
print(student)
# => {'name': 'Carlos', 'course': 'SEI'}
len(student)
# => 2
len({})
# => 0


# Iterating Item

'''
for ... in loops are used to iterate over items in a dict.
'''
# accessing the value of an item as follows is considered to be an ANTI-PATTERN:

for key in student:
    print(f"{key} = {student[key]}")

# the preferred approach is to use the items() method to obtain a dictionary view object.

student.items()
# => dict_items([('name', 'Carlos'), ('course': 'SEI')])

# now we can use a for ... in loop to iterate over the view obj

for key, val in student.items():
    print(f"{key} = {val}")
