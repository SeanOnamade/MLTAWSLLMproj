# If you don't know how many arguments will be passed to your function, you can use *args for positional arguments (i.e. listed as multiple vars)
# and **kwargs for keyword arguments (can be accessed with .items()).

# def make_pizza(*toppings):
#     print("Now we're cooking! Making a pizza with the following toppings...")
#     for topping in toppings:
#         print(f"- Add some {topping}")
#     print("Done! Enjoy!")

# make_pizza("pepperoni", "mushrooms", "green peppers")


# Program to add and display the sum of n number of integer
# def add(*num):
#     sum = 0;
#     for n in num:
#         sum = sum + n;
#     print("Sum:", sum)

# add(2,6)
# add(3,4,5,6,7)
# add(1,2,3,5,6,7,8)

# def build_profile(first, last, **user_info):
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile

# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
# print(user_profile)


# # Print values of function Person along with its associated keywords
# def Person(**kwargs):
#     for key, value in kwargs.items():
#         print("{} -> {}".format(key, value))    # OR print(f'{key} -> {value}')

# Person(Name = 'Sean', Sex = 'Male', Age = 38, City = 'London', Mobile = 9375821987)


# args must always be mentioned before kwargs if used together
# def func(a, b, *args, option = False, **kwargs):
#     print(a, b)
#     print(args)
#     print(option)
#     print(kwargs)

# func(1, 3, 10, 20, Name = 'Tom', Salary = 60000)

# OBJECTS
# Class: A blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.
# Object: An instance of a class. It represents a specific entity with attributes and behaviors defined by the class.
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         return "Woof!"

# my_dog = Dog("Buddy", 3)
# print(my_dog.name)  # Output: Buddy
# print(my_dog.age)  # Output: 3
# print(my_dog.bark())  # Output: Woof!

# ENCAPSULATION
# Encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data into a single unit, or class. 
# It restricts direct access to some of the object's components, which can prevent the accidental modification of data.
# class Car:
#     def __init__(self, make, model):
#         self.__make = make  # Private attribute
#         self.__model = model  # Private attribute

#     def get_make(self):
#         return self.__make

#     def set_make(self, make):
#         self.__make = make

# my_car = Car("Toyota", "Corolla")
# print(my_car.get_make())  # Output: Toyota

# INHERITANCE
# Inheritance allows a class to inherit attributes and methods from another class. 
# This helps in reusing code and creating a hierarchical relationship between classes.

# class Animal:
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# my_dog = Dog()
# my_cat = Cat()
# print(my_dog.speak())  # Output: Woof!
# print(my_cat.speak())  # Output: Meow!

# POLYMORPHISM
# Polymorphism allows methods to do different things based on the object it is acting upon. 
# It means "many forms" and allows the same method to be used on different objects.
# class Bird:
#     def fly(self):
#         return "Flying high!"

# class Penguin(Bird):
#     def fly(self):
#         return "I can't fly!"

# Tom = Bird()
# Tim = Penguin()
# print(Tom.fly())  # Output: Flying high!
# print(Tim.fly())  # Output: I can't fly!

from abc import ABC, abstractmethod
# abc is a module for defining abstract base classes. ABC is a helper class for defining them, and abstractmethod is a decorator for abstract methods


class Shape(ABC): # Shape is defined as a subclass of ABC, making it an abstract base class
    @abstractmethod # indicates the method is abstract and thus must be implemented by a non-abstract subclass of 'shape'. 
    # W/o it, area method is no longer considered abstract
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self): # every subclass of Shape requires an area method; instantiating w/o it gives a TypeError
        return self.width * self.height

my_rectangle = Rectangle(3, 4)
print(my_rectangle.area())  # Output: 12

