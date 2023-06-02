# ========== Conditional Expressions In Python ========= #

# Boolean Values
'''
Python has two logical boolean values: True and False/

Most logical operations reslt in one of those two values.
'''

# Truthy and Falsy
'''
Every expression in Python is considered to be Truty or Falsy

Most things in Python are considered to be Truthy
'''

# Falsy in Python:
False
None
0
0.0
0j
# Empty sequences or collections are falsy
''  # empty string
[]  # empty list
()  # empty tuple
{}  # empty dictionary
range(0)  # empty range


# Comparison Operators:
# < #less than
# > #greater than
# <= #less than or equal to
# >= #greater than or equal to
# == #equal to
# != #not equal to

8 > 8
# => False — 8 is not greater than 8.

8 >= 8
# => True — This checks if 8 is greater than or equal to 8, and they are equal.

8 < 8
# => False — 8 is not less than 8.

7 == 7
# => True — 7 is equal to 7.

7 == "7"
# => False — One is a number and the other is a string.

7 != 7
# => False — This checks if they aren't equal. Because does 7 equal 7, it's `False`.

6 != 7
# => True — 6 is not equal to 7.

# Logical Operators

# or is the same as ||; if the first operand is truty, return it, otherwise return second operand
# and is the same as &&; if the first operand is falsy, we will return its value, if the first operand is truthy, we will return the value of the second operand

True or False
# => True

False or True
# => True

'hello' or 0
# => 'hello'

0 or 'hello'
# => 'hello'

True and False
# => False

False and True
# => False

'hello' and 0
# => 0

0 and 'hello'
# => 0

'hello' and 'tacos'
# => 'tacos

# not 'flips' truthiness/falsiness of its operand, adn returns True or False

not True
# => False

not 124
# => False

not []
# => True

# ========== Branching ========= #
'''
Python uses indentation instead of {} to define blocks of code

proper indentation is mandatory

'''

# branching with the if statement

floor = 'sticky'
walls = 'clean'

if floor == 'sticky':  # dont forget colon :
    print("Clean the floor! It's sticky!")
    # more lines of code in this code
    # block needs to be indented as well
if walls == 'sticky':
    print("Clean the walls! They're sticky!")


# dual path if..else statement:
condition = "my condition"
if condition:
    # do something
    print('Nice')
else:
    # do something else
    print('Not Nice')

# multi-path if..elif..else statement:
condition1 = "my condition"
condition2 = "my condition"
condition3 = "my condition"

if condition1:
    print('first')
elif condition2:
    print('second')
elif condition3:
    print('third')
else:
    print('none of the above')


color = input("Enter 'Green', 'yellow', 'red', or 'quit': ").lower()
print(f'The user entered {color}')

# ========== Looping ========= #

# for loop
'''
Python for loop always iterates over the items in a sequence, similar to JS for...in and for...of loops
'''
names = ['Carlos' 'Juan', 'Shirley', 'Abraham', 'Alejandra']

for name in names:
    print(f'{name} is a strong, capable person!')

# while loops
'''
Python while loops continue to iterate while a given condition is truthy
'''

while condition:
    print('do some stuff')

# while loops are the go to when the number of times you will need to iterate is unknown
# Watch out for infite loops by making sure a condition returns falsy at some point so that the loop exits.

# Break Statement

'''
the break statement is used to immediately exit for and while loops and continue executing any statements that may follow them
'''

# continue statement
'''
continue statement isused to return to the top of the for or while loop. 

In case of while loop, the conditional expression is reevaluated to determine if the loop should continue
'''
while True:
    color = input("Enter 'Green', 'Yellow', 'Red', or 'Quit': ").lower()

    if color == 'green':
        print(f'You selected {color}, the color of nature')
    elif color == 'yellow':
        print(f'You selected {color}, the color of the sun')
    elif color == 'red':
        print(f'You selected {color}, the color of roses')
    elif color == 'quit':
        print('Exiting the program.')
        break
    else:
        print('Unknown selection, please try again.')

# ========== Python Ranges ========== #
'''
Python ranges aere sequence types like lists and types

the range type representes an immutable sequence of integers... commonly used for looping a specific number of times in for loops

Ranges have class type of range.
'''
# Ranges - basic syntax

for num in range(5):
    print(num)
# => 0
# => 1
# => 2
# => 3
# => 4

# ranges can also generate sequences with a start and a step

for even in range(2, 10, 2):
    # (start, range, step)
    print(even)
    # => 2
    # => 4
    # => 6
    # => 8

# when not passed in, start defaults to 0 and step defaults to 1


# range can also be used to create lists and tuples:

nums = list(range(10))
print(nums)
# => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odds = tuple(range(1, 10, 2))
print(odds)
# => (1, 3, 5, 7, 9)

# Ranges - Negative step; if step is a negative integer, the sequence counts down

for num in range(5, 0, -1):
    print(num)
    # => 5
    # => 4
    # => 3
    # => 2
    # => 1
