#Single Inheritance
class Animal:                #parent
    def __init__(self):
        print("Welcome")
    def walk(self):
        print("The animal walks")

class Dog(Animal):           #child
    def eat(self):
        print("The dog eats")

A=Animal()
A.walk()

D=Dog()
D.eat()
D.walk()