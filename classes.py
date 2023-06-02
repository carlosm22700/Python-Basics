# ========== Classes ========== #
'''
Python is an OOP language

Object-Oriented programming is characterized by programming with objecs that represent the real-world objects of the application
'''

# Classes act like 'Blueprints' and are used to create objects.

# Encapsulation refers to the bundling of related properties (attributes) and methods (behavior) together in an object.


# ========== Objects in Python ========== #
# eveyrhting in Python is an obj
# python provides a dir() function that can be used to list an obks members

# create a list
nums = [1, 2, 3, 4]
# print the attributes and methos nums has
print(dir(nums))
'''
Output:
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''

# ========== Writing a basic Python class ========== #


class Dog():  # naming convention for python classes is UpperCamelCasing
    def __init__(self, name, age=0):  # python calls on the __init__ magic method when a new dog instance is created; this is short for initialize because the methos is used to initialize the properties of a new obj
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name} says woof!')

# the age = 0 in __init__'s parameter list is called a default parameter and will be assigned the result of the expresion to the right of the =, if the function is called without an argument for that positional parameter

# the attributes for a dog instance are name and age.

# bark is an instance method in this Dog class


'''
What is self?

-enables a method to access the other properties/methods in an object
-enabes a single-copy of a method in memory to serve any number of instances.

since the first parameter is named first...

when we write code like spot.bark(), the obkect to the left of the dot is automatically passed by Python as the first argument

This is how Python provides method's context in both instance and class methods
'''


# ========== Creating Objects by Instantiating a Class ========== #
# by defining a Dog class, we know the strucutre that each input will have

spot = Dog('Spot', 8)

print(spot)

# print the name and age attributes of the spot obj
print(spot.name, spot.age)
# => Spot 8

# Invoke the spot object's bark instance method
spot.bark()
# => Spot says woof!

# 👀 Unlike dictionaries that use [] to access/set its items' values, objects instantiated by our own Python classes use dot notation instead.

# testing out default parameter for a new dog's age:

dog = Dog('Aiko')

print(dog.name, dog.age)
dog.bark()
# => Aiko 0
# => Aiko says woof!

# ========== Overriding Methods ========== #

# we can ovveride the __str__ method that the print function calls, in order to obtain the string when running print(spot)


class Dog():
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name} says woof!')

    def __str__(self):
        return f'Dog named {self.name} is {self.age} years old'


aiko = Dog('Aiko', 3)
print(aiko)
# => Dog named Aiko is 3 years old


# ========== Class vs. Instance Members ========== #
'''
In Python, instance attributes & methods are intended to be accessed by instances of the class

Class members are intended to be accessble on the class only, not instance.

This means the class attributes are shared with all insantiations of the Dog class, while instance variables are only usable within the instance, or current instantiation, of a given dog class.

- Each object has its own copy of its instanc eattributes (name, age, etcc).
-Class methods/attributes are shared by all instances of that class. (e.g. bark, etc...)
'''

# we can add next_id class attribute that can be used to assign an id to each object


class Dog():
    # class attribute
    next_id = 1

    # updated __init__
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.id = Dog.next_id
        Dog.next_id += 1

    def bark(self):
        print(f'{self.name} says woof!')

    # updated __str__
    def __str__(self):
        return f'Dog ({self.id}) named {self.name} is {self.age} years old'

    @classmethod
    def get_total_dogs(cls):
        # cls represented the dog class
        return cls.next_id - 1


'''
1) the @classmethod decorater
2) the naming convention of the first parameter to use cls instead of self

👀 Decorators in programming are a way of metaprogramming (program has knoweldge of, or manipulates itself). In Python, decorators are used to modify the behavior of a function or class. 
'''

aiko = Dog('aiko', 3)
print(aiko)
tsuki = Dog('tsuki', 2)
print(tsuki)

print(Dog.get_total_dogs())
# => 2


# ========== Inheritance ========== #

'''
using inheritance, a subclass automaticall inherits all of the attributes and methods of its superclass.

the subclass can define addition attr./methods to make it more specialized class than the superclass

'''

# Pass in superclass as argument


class ShowDog(Dog):
    # add additional parameters AFTER those in superclass
    def __init__(self, name, age=0, total_earnings=0):
        # always call the superclass init first.
        Dog.__init__(self, name, age)
        # Now add any new attributes
        self.total_earnings = total_earnings

    # add additional methods
    def add_prize_money(self, amout):
        self.total_earnings += amout
        print(f'{self.name}\'s new total earnings are ${self.total_earnings}')


winky = ShowDog('Winky', 3, 1000)
print(winky)  # Yay, inherited the overriden __str__
winky.bark()  # inherited the bark method
print(winky.total_earnings)
# => 1000
winky.add_prize_money(500)  # New method that Dogs doesnt have
print(winky.total_earnings)
# => 1500
