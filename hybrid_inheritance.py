#Hybrid inheritance =======Combination of two or more types of inheritance
class Animal:                #parent ---------
    def eat(self):              #            |
        print("Animal eats")    #            |
class Dog(Animal):          #child ------------------ Hierarchial Inheritance
    def bark(self):             #            |
        print("Dog barks")      #            |
class Cat(Animal):          #child------------
    def meow(self):         #                |
        print("Cat meows")  #                |
class pet(Dog,Cat):         #child -------------------- Multiple Inheritance
    def info(self):
        print("This is a pet")
p=pet()
p.eat()
p.bark()
p.meow()
p.info()

