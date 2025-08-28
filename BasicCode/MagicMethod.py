class Per:
    pass

p=Per()
print(dir(p)) # These are the magic method


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name}, {self.age} yrs old"

    def __repr__(self):
        return f'Person (name={self.name}, age={self.age})'

person=Person('Sahil',27)
print(person)
print(repr(person))

#### Common Operator Overloading Magic Methods

class Vector():
    def __in__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Vector


