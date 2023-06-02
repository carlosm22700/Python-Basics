# ========== Lists ========== #
'''
lists are to Python as arrays are to JS

A list provides a container for zero or more items

Lists can contain items of different types, including dictionaries and nested lists

Lists have a class (type) of list
'''

# ========== Basic Syntax ========== #

colors = ['red', 'green', 'blue']

# number of items in a list can be returned using the built-in len() function

len(colors)
# => 3

# ========== Features ========== #
''' 
List are considered to be a sequence type in Python

A sequence is a generic term used for an ordered collection. 

Other types include strings and tuples

Lists are mutable:
-existing items can be updated
-items can be added to the list
-items can be removed from list
'''

# ========== Accessing Items ========== #

# we can use square brackets to access items in a list

idx = 1
colors[idx + 1]
# => blue

# we can also use negative integers to access from the end of a list

colors[-1]
# => blue

# No need to write colors[len(colors) - 1]

# ========== Assigning Items ========== #

# we use square bracks to target an item of a list for assignment

colors[-1] = 'brown'
print(colors)
# => ['red', 'green', 'brown']

# unlike in  JS, assigning to a non-exisiting index results in an error:

colors[10] = 'Yellow'
# => IndexError: list assignment index out of range


# ========== Adding an Item ========== #

# the equivalent to the JS push method is append()
colors.append('purple')

# it only adds one item and does not return the new value

# we use the extend() method to add multiple values

colors.extend(['orange', 'black'])

# or the += operator

colors += ['orange', 'black']

# the + operator can be used to create a new list by combining others

odds = [1, 3, 5]
evens = [2, 4, 6]
nums = odds + evens
print(nums)
# => [1, 3, 5, 2, 4, 6]

# Inserting an Item using insert() method

print(colors)
# => ['red', 'green', 'brown', 'purple', 'orange', 'black']

colors.insert(1, 'yellow')
# => ['red', 'yellow,' 'green', 'brown', 'purple', 'orange', 'black']


# ========== Removing an Item ========== #

'''
Python has a pop() method for removing an item

it is more flexible in Python because you can specify the index of the item to remove and return
'''

print(colors)
# => ['red', 'yellow', 'green', 'brown', 'purple', 'orange', 'black']

green = colors.pop(2)
print(colors)
# => ['red', 'yellow', 'brown', 'purple', 'orange', 'black']

# If value returned by pop is not important, we can also use del operator
print(colors)
# => ['red', 'yellow', 'brown', 'purple', 'orange', 'black']
del colors[1]
print(colors)
# => ['red', 'brown', 'purple', 'orange', 'black']


# remove() method that removes the first item that matches what's passed in

print(colors)
# => ['red', 'brown', 'purple', 'orange', 'black']
colors.remove('orange')
print(colors)
# => ['red', 'brown', 'purple', 'black']

# no value is returned by the remove() method

# ========== Clearing an Entire List ========== #

print(colors)
# => ['red', 'brown', 'purple', 'black']
colors.clear()
print(colors)
# => []

# ========== Iterating Over Items in List ========== #

# For... in loop is used to iterate over items in a list

colors = ['red', 'green', 'blue']
for color in colors:
    print(color)
# => red
# => green
# => blue

# if we need to access the index of the item while iterating we can use the enumerate() function to provide the index and value to a for... in loop

for idx, color in enumerate(colors):
    print(idx, color)
# => 0 red
# => 1 green
# => 2 blue


# ========== List Comprehensions ========== #

'''
Purpose: 

Powerful feature in Python. They provide a concise way to create and work with lists.
'''

# Numerical example

# if we need to square all of the numbers ina list and put them in a new list, we might use a for loop like this:

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n * n' for each 'n' in nums

squares = []
for n in nums:
    squares.append(n * n)
print(squares)
# => [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# In Javascript, we woud use the map() method 👆🏽

# A list comprehension can reduce the code:

squares = [n * n for n in nums]  # this always returns a new list

'''
BASIC SYNTAX: 

# [<expression> for <item> in <list>]
# This reads as: I want <expression> for each <item> in <list>

this is basically a modified for...in loop within square brackets that returns a new list.
'''

# ========== Filtering the Items ========== #

# non-comprehension appraoch using a for...in to map and filter nums:

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n * n' for each 'n' in nums if 'n * n' is even

even_squares = []
for n in nums:
    square = n * n
    if square % 2 == 0:
        even_squares.append(square)
print(even_squares)
# => [4, 16, 36, 64, 100]

# Reduced using list comprehension:

even_squares = [n * n for n in nums if (n * n) % 2 == 0]


# ========== Slice Assignment in Lists ========== #
'''
we cann use the slice operator to insert and/or remove items in a list; similar to splice() in JS

'''

chars = ['a', 'b', 'x', 'y', 'd']

# we cna replace the 'x' and 'y' chars with 'c' like this

chars = ['a', 'b', 'x', 'y', 'd']
chars[2:4] = 'c'
print(chars)
# => ['a', 'b', 'c', 'd']

'''
Our resuting list is smalelr than the original list. 
items on index locations, 2, 3, up to but not including 4, are replaced with 'c'
'''
