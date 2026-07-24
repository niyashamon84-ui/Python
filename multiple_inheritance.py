#Multiple Inheritance==== two parents
class Mother:                #parent
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info1(self):
        print(f"Name:{self.name},Age:{self.age}")
    def talent(self):
        print("Mother is cooking")
class Father:                #parent
     def __init__(self,name1,age1):
          self.name1=name1
          self.age1=age1
     def info2(self):
         print(f"Name:{self.name1},Age:{self.age1}")
     def skills(self):
        print("Father is driving")
class child(Mother,Father):         #child
    def play(self):
        print("The child is playing")

C=child("Sheela",52)
C.info1()
C.talent()
#C.info2()
C.skills()
C.play()
    
         
  

