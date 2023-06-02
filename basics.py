import math
# This is a comment !

# anything after the # will not be run

total_guitars = 7  # Hope someone knows how to play guitar

# multiline comment in python:

"""
This is a
multiline comment
"""

# ========== variables ========= #

# my_var - this will return an error (illegal syntax)
# my_variable = 1

my_number = 14
print(my_number)
my_number = 11
print(my_number)

# ========== Naming Conventions ========= #
# casing does matter!
first_name = 'carlos'

# ===== Data Types =====#
# checking the data type of an obj
'''
we use the type() function to obtain the class used to instantiate the data:
'''
print(type(42))  # <class 'int'>
print(type('hello'))  # <class 'str'>
print(type(True))  # <class 'bool'>

# in python, we convert non-integer numbers into integers using the  int() function:

a_float = 1.7
an_int = int(a_float)
print(an_int)  # 1

'''
Nums with a decimal point are stored in variables as floating-point numbers, usually just called a float. 
'''

# Certain built-in features need to be imported
# import math - already imported at top due to prettier

pi = math.pi
pi  # 3.141592

type(pi)  # <class 'float'>
some_float = 25.
type(some_float)  # <class 'float'>

# complex nums
'''
python has a data type for complex nums, i.e, numbers with an 'imaginary' component usually obtained by taking the square root of a negative number

The imaginary portion is represented by the letter 'j'
'''

my_complex = 3+4j
type(my_complex)  # <class 'complex'>

# Booleans
'''
Logical data types often used in conditional expressions - Identifiers are capitalized
'''

my_bool = True
my_other_bool = False
type(my_bool)  # <class 'bool'>

# Nothingess
'''
pythons equivalent to JS Null and undefined
'''

my_nothing = None
type(my_nothing)  # <class 'NoneType'>

# ========== Math Operations ========= #
'''
Python has:
-Addition (+)
-Subtraction (-)
-Multiplication (*)
-Division (/)
-Modulo (remainder) (%)
-Exponentiation (**)
'''

# Integer Division
'''
You can force the result to be an integer when dividing two integers using // instead of /
'''

quotient = 5 // 2
quotient
2  # 2 is printed, because decimal '.5' is truncated

# ========== Shortcut Assignment Operators ========= #
'''
Reasigning to a variable the result of adding, etc. to that var is common.

python has operators that make it cleaner to write
'''

# This line of code...
num = num + 1
# ...can be written with this shortcut operator:
num += 1

# It also works for any of the other math operations:
num = num / 5
# Rewrite like this:
num /= 5

# And this...
num = num * 3
# Can be written as this...
num *= 3
# And so on with the other operators.

# (++) and (--) do not exist in python so we use +=1 and -=1

# ========== Ternary Expressions ========= #

'''

In JS:
// Using the ternary operator/expression
let beverage = age >= 21 ? 'Beer' : 'Milk';

// Without a ternary expression
let beverage;
if (age >= 21) {
  beverage = 'Beer';
} else {
  beverage = 'Milk';
}

Python does not have a dedicated ternary operator

instead python uses a modified syntax of if... else which results in a ternary expression instead of a control flow construct.

'''
age = 21

beverage = 'Beer' if age >= 21 else 'Milk'

# ========== Converting Between Data Types  ========= #
'''
Python does not have type coercion. 

doing math operations between integers and floats is allowed, but not much else.

python provides us with predefined classes to do so:

'''

str(item)        # Converts item to a string
int(item, base)  # Converts the provided item to an integer with the provided base
float(item)      # Converts the item to a floating-point number
hex(int)         # Converts an integer to a hexadecimal STRING
oct(int)         # Converts an integer to an octal STRING
tuple(item)      # Converts item to a tuple
list(item)       # Converts item to a list
dict(item)       # Converts item to a dictionary

# ========== Working with Strings  ========= #

# python has strings for holding text:

my_string = 'A single quoted string'
your_string = "A double quoted string"

# you can also do multi-line strings by using a tripe quote (single or double)

multiline_string = ''' This is my string to goes 
on multiple lines
for whatever reason.'''

# ========== Concatenating Strings  ========= #
# strings can be combined using the  + operator

little_string = 'bad'
medium_string = 'super'
long_string = medium_string + little_string
print(long_string)  # 'superbad'

# ========== Strings Interpolation ========= #

state = 'Hawaii'
year = 1959
message = f'{state} was the last state to join the U.S in {year}'

# older versions used the string format method

template = 'My name is {} and I like {}'
print(template.format('Carlos', 'Tacos'))
# prints 'My name is Carlos and I like Tacos'

# ========== Useful String Methods  ========= #

'Ace of spaces'.split(' ')
# => ['ace', 'of', 'spades']

# However, this wont work as desired
'abcd'.split('')
# instead, use the list() function:
list('abcd')
# => ['a', 'b', 'c', 'd']

# WARNING: Raises an erorr if substring is not found
'tesla'.index('s')
# => 2

# Like index, but returns -1 if substring not found:
'tesla'.find('x')
# => -1

'foo'.upper()
# => 'FOO'

'WHY?'.lower()
# => 'why?'

'Then I went to the store I like'.replace('I', 'We')
# => 'Then we went to the store we like'


# to know if a string contains a substring we can use the in operator

'eggs' in 'green eggs and ham'
# => True

# use built in global len()function on a string to find its length

len('Tacos')
# => 5


# ========== Pythons built in functions  ========= #

'''
Notice we did not call len() as a method on a string like this:

'Tacos'.len()

len() is one of the several built in Python functions

len(arg), is a function that return the length of an obj. The argument may be a sequence or collection

in Python a string is a sequence of characters.

B/c a string is a sequence, we can use [] to access each character in the string:

'''

course = 'SEI'
print(course[0])
# => Prints 'S'

# We can also use negative indexes!
last_letter = course[-1]
print(last_letter)
# => Prints 'I'


# Although we can access individual characters in a string, we cannot update the individual chars because strings are immutable

s = 'Hello'
s[0] = 'J'

'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
'''
