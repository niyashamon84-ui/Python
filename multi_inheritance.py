#Multilevel Inheritance ===grandparent,parent,child
class Animal:                   #grandparent
    def __init__(self):
        print("Hello")
    def walk(self):
        print("The animal walks")
class Cat(Animal):             #parent
    def eat(self):
        print("The cat eats")
class Kitten(Cat):             #child
    def runs(self):
        print("The kitten runs")

K=Kitten()
K.walk()
K.eat()
K.runs()


