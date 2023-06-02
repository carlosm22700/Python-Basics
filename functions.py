# ========== Python Functions  ========= #
# function syntax:
def fahr_to_kelvin(temp):
    return ((temp - 32) * (5/9)) + 273.15

# def keyword, that defines a fuction
# name (identifier) of the function.
# parameter list inside paratheses
# the first line ends with semicolon
# first line is followed by indented code block that we have become familiar with.
# Optionally return a value with the return statement

# ========== Minimal Function in Python  ========= #

# this is how we stub up a function in python


def first_function():
    pass  # 'do nothing' statement and is useful to create a function that has at least one statement in its block


# assign value returned by default
result = first_function()
print(result)
# => None ; this is returned when the function doesn't have a return statement

# ========== Key Differences Between Python and JS Functions ========== #


'''
Python functions are similar to function definitions in JS - Not function expressions.

They cannot be assigned to variables at the time they are being defined:

This does not work:

my_function = def my_function():
    pass
    
'''

# after being defined, functions can be assigned to variabes, referenced by dicts./lists, etc.

# Dynamically 'select' which function to call using a dictionar instead of a nested if...elif...else statement:


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


math_operations = {
    '+': add,
    '-': subtract
}

selected_operation = '+'

math_operations[selected_operation](2, 4)
# => 6

'''
Python does not hoist functions

# Will cause an error - must call function AFTER it has been defined
add(5, 10)

def add(a, b):
  return a + b

'''

# ========== Lambda Functions ========== #
'''
Python has lambda functions, which are like Arrow Functions in JS:

-they implicitly return a single expression's value
-They are expressions, so they are commonly used as in-line arguments.
they can be assigned to a variable

** Unlike arrow functions, they cannot have any code block - just a single expression that has its result implicitly returned

JavaScript:
const nums = [1, 3, 2, 6, 5];
let odds = nums.filter(num => num % 2);
'''
# Python:
nums = [1, 3, 2, 6, 5]

odds = list(filter(lambda num: num % 2, nums))

# ========== Calling Functions ========== #

# we call functions the same as it is in JS


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def compute(a, b, op):  # functions can be passed to other functions as callbacks
    return op(a, b)


print(compute(1, 2, add))

# ========== Parameters & Arguments ========== #
# parameters are the placeholders for passing input to a function.


def add(a, b):  # a & b are parameters
    return a + b


num = 5

add(num, 10)  # num and 10 are arguments

# Python requires that the correct number of arguments be provided when calling a function


def add(a, b):
    return a + b


add()
# => TypeError: add() missing 2 required positional arguments: 'a' and 'b'

# ========== Accepting Varying Number of Arguments ========== #

# * 'star' specifier in a parameter list allows us to pass in a varying number of positional arguments to a function


def fn(*args):
    print(type(args))
    for arg in args:
        print(arg)


fn(1, 2, 'SEI')
'''
<class 'tuple'>
1
2
SEI
'''
# The identifier used with *, (args), can be anything. By convention we use args
# Always use args after any required positional parameters:


def dev_skills(dev_name, *args):
    dev = {'name': dev_name, 'skills': []}
    # args will be a tuple
    for skill in args:
        dev['skills'].append(skill)
    return dev


print(dev_skills('Alex', 'HTML', 'CSS', 'JavaScript', 'Python'))
# => {'name': 'Alex', 'skills': ['HTML', 'CSS', 'JavaScript', 'Python']}

# we can also use the list() function to convert hte args tuple into a list


def dev_skills(dev_name, *args):
    dev = {'name': dev_name, 'skills': list(args)}
    return dev


# ========== Python's * Parameter Specifier (*kwargs) ========== #
'''
kwargs = keyword arguments

a kwarg is an argument with a name, also referred to as named arguments
'''


def divide(a, b):
    return f'{a} divided by {b} is {a / b}'


divide(b=25, a=100)
# => '100 divided by 25 is 4.0'

# above example is not how kwargs are commonly used ...

# we use ** specifier when defining a parameter named **kwargs. By adding it at the end of the parameter list, we can access any number of keyword arguments


def dev_skills(dev_name, **kwargs):
    # kwargs will be a dictionary
    dev = {'name': dev_name, 'skills': kwargs}
    return dev


print(dev_skills('Jackie', HTML=5, CSS=4, JAVASCRIPT=4, Python=2))

# ========== Combining Required Positional, Optional Positional (args) & **kwargs Arguments ========== #

# you can use all three types of parameters in the same function, but they have to be defined as follows:


def arg_demo(pos1, pos2, *args, **kwargs):
    print(f'Positional params: {pos1}, {pos2}')
    print('*args:')
    for arg in args:
        print('', arg)
    print('**kwargs:')
    for keyword, value in kwargs.items():
        print(f' {keyword}: {value}')


arg_demo('A', 'B', 1, 2, 3, color='purple', shape='circle')

# => Positional params: A, B
# => *args:
# => 1
# => 2
# => 3
# => **kwargs:
# =>    color: purple
# =>    shape: circle
