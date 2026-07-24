class Animal:                         #parent
    def __init__(self,breed,colour):
        self.breed=breed
        self.colour=colour
    def info(self):
        print(f"Breed:{self.breed},Colour:{self.colour}")

class Dog(Animal):                   #child
    def eat(self):
        print("The dog eats")

D=Dog("Dash Hound","Brown")
D.eat()
D.info()
