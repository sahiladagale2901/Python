from BasicCode.venv.Lib.tkinter.font import names


class Person:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('sahil', 27)
print(p1.name, p1.age)


################# Define class with instance method

class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def food(self):
        if self.name == 'sahil':
            print(f"{self.name}: Veg")
        else:
            print(f"{self.name}: Non veg")


pe1 = People('sahil', 27)
pe1.food()


############################### Modeling and Banking Acc

class BankAc:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Hello {self.owner}\n{amount} is deposited, new balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Hello {self.owner}\nInsufficient funds")
        else:
            self.balance -= amount
            print(f"Hello {self.owner}\n{amount} is withdraw, remaining balance is {self.balance}")

    def get_balance(self):
        return self.balance


ac = BankAc('Sahil')
ac.deposit(5000)
ac.withdraw(2000)
print(ac.get_balance())


#####################################################################################################################

### INHERITANCE OOPs

class Parent:
    def __init__(self, parameter1):
        self.parameter1 = parameter1

    def method1(self):
        print("method 1 from parent")


class Child(Parent):
    def __init__(self, parameter1, parameter2):
        super().__init__(parameter1)
        self.parameter1 = parameter2

    def method2(self):
        print("method 2 from child")


child = Child('par1', 'par2')
child.method1()
child.method2()


######### Multiple Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('Subclass must implement this method')


class Pet:
    def __init__(self, owner):
        self.owner = owner


class Dog(Animal, Pet):
    def __init__(self, name, owner):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)

    def speak(self):
        return f"{self.name} say woof"


dog = Dog('Buddy', 'Sahil')
print(dog.speak())


#####################################################################################################################
### POLYMORPHISM OOPs
# single action in different form

# Method Overriding -> child class provide a specific implementation of method
# tht already in Defined Parent class

# Base class
class Animal:
    def speak(self):
        return "Sound of an animal"


# Derived class
class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


## Function that demonstrates polymorphism

def animal_speak(a):
    print(a.speak())


dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())
animal_speak(dog)


#### Function and Method

class Shape:
    def area(self):
        return "The area of the fig"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.142 * (self.radius ** 2)


#### Function that demonstrate polymorphism

def print_area(shape):
    print(f"the area is {shape.area()}")


rect = Rectangle(2, 4)
circle = Circle(4)

print_area(rect)
print_area(circle)

#####################################################################################################################
# Polymorphism with Abstract Base class

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        return "Car Start"


class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle Start"


def start_Engine(vehicle):
    return f"{vehicle.start_engine()}"


car = Car()
motorcycle = Motorcycle()

print(start_Engine(car))


####################################################################################################################

### Encapsulation

class Person():
    def __init__(self, name, age):
        self.name = name  ## Public variable
        self.age = age  ## Public variable


def get_name(per):
    return per.name


person = Person("Sahil", 27)
# print(person.name)

print(dir(person))


### Encapsulation
################################### Private variable
class Person():
    def __init__(self, name, age):
        self.__name = name  ## private variable  -> __variable
        self.__age = age  ## private variable


class Em(Person):
    def __init__(self, name, age,gender):
        super().__init__(name, age)
        self.gender = gender

# def get_name(per):
#     return per.__name


person = Person("Sahil", 27)
# print(person.name)

## Error -> Attribute Error bcz private variable
# print(get_name(person))

em=Em("Sahil", 27,"M")
print(get_name(em.__name))
