#Hierarchial inhertance =====single parent,multiple child
class Animal:              #parent
    def walk(self):
        print("The animal walks")
class Dog(Animal):         #child
    def eat(self):
        print("The dog eats")
class Cat(Animal):         #child
    def run(self):
        print("The cat runs")
d=Dog()
c=Cat()
d.walk()
d.eat()
c.walk()
c.run()
c.eat()
