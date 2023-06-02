# ========== Tuples ========== #
'''
tuples are very similarto Python lists.

Tuples have a class (type) of tuple

tuples might be 'classified' based on how many items they contain, e.g., a 2-tuple would contain two items such as (some_key, some_value)
'''

# ========== Basic Syntax ========== #

colors = ('red', 'green', 'blue')
print(colors)
# => ('red', 'green', 'blue')
print(len(colors))
# => 3

# paranthesis are optional:

colors = 'red', 'green', 'blue'

# comma is necessary if we want to create a 1-tuple

# will not create a tuple
hello_tuple = ('Hello')
print(type(hello_tuple))
# => <class 'str'>

hello_tuple = ('Hello',)
# or the following:
hello_tuple = 'Hello'
print(type(hello_tuple))
# => <class 'tuple'>

# ========== Difference Between Tuples and Lists ========== #
'''
The main difference b/w tuples and lists is that tuples are immutable

since tuples can't be changed after they are created, they are great for protecting data that you dont want to be changed

because they cannot be changed, they can be used as keys in dicts.

Tuples are generally used to contain different data types and lists for similar data types.

'''

# ========== Accessing Items ========== #
# although tuples cannot be modified, we retrieve their items in the same way using square brackets:

colors = ('red', 'green', 'blue')
green = colors[1]
print(green)
# => green

# sequences have an index() method that returns the index of the first match
colors = ('red', 'green', 'blue')
blue_idx = colors.index('blue')
print(blue_idx)
# => 2

# ========== Iteration ========== #

# we can iterate using a for ... in loop
colors = ('red', 'green', 'blue')

for idx, color in enumerate(colors):
    print(idx, color)
# => 0 red
# => 1 green
# => 2 blue

# ========== Slicing (Copying) Sequences ========== #
'''
slicing is used to create 'slices' of sequences

Python uses this syntax:

a_sequence[start:end:step]
'''

short_name = 'Alexandria'[0:4]
print(short_name)
# => Alex
# note that slice includes up to, but not including the index to the rigt of the colon

# if first index is ommited, the default start index of 0 is used

colors = ('red', 'green', 'blue')
print(colors[:2])
# => ('red', 'green')

# if the up to sequence is ommitted, the slice copies the sequence all of the way up to the end:
colors = ['red', 'green', 'blue']
print(colors[1:])
# => ['green', 'blue']

fruit = ('apple' 'banana', 'pear')
fruits = fruit[:]
# => ('apple', 'banana', 'pear')


# ========== Unpacking Tuples ========== #

'''
Unpacking allows you to perform multiple variable assignments ina  single line of code
'''


colors = ('red', 'green', 'blue')
r, g, b = colors
print(r, g, b)
# => red green blue

# comma separated variables on the left-side of the assignment operator and a sequence of vaues on the right is what it takes
# we've seen it below with for in loops:

student = {
    'name': 'Carlos',
    'program': 'SEI'
}

for key, val in student.items():
    print(f"{key} = {val}")
