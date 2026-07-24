class student:
     def __init__(self):
         print("The object is called")
     def study(self,name):
         print("Hey",name)
S1=student()
S1.study("Niya")

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def read(self):
        print(f"Name:{self.name},Age:{self.age}")
S1=student("Niya",22)
S1.read()



