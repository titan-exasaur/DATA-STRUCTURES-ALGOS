# OBJECT ORIENTED PROGRAMMING IN PYTHON


### OBJECT

object = A "bundle" of attributes(variables) and methods(functions)

e.g., phone, cup, book

you need a "class" to create many objects. class --> a blueprint used to design the structure and layout of an object

### CLASS VARIABLES

class variables --> shared among all the variables

It is defined outside the constructor, it allows you to share data among all the objects created from that class

```
class Car:

    wheels = 4 <-- class variable

    def __init__(self, model, year):
        self.model = model  <-- instance variable
        self.year = year   <-- instance variable
```

### INHERITANCE

Inheritance allows a class to inherit attributes and moethods from another class. 
This helps with code reusability and extensibility.

```
class Animal: <-- base class / Super class
    def __init__(self, name):
        self.name = name

class Dog(Animal): <-- derived class / sub class
    pass

class Cat(Animal): <-- derived class / sub class
    pass
```

### MULTIPLE INHERITANCE

Multiple inheritance is when a class can inherit from more than one parent class

C(A,B)

### MULTILEVEL INHERITANCE

Multilevel inheritance is when a class inherits from a parent which inherits from another parent class

C(B) <- B(A) <- A