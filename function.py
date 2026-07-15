#Function with no input
def hello():
    print("helo")
hello()

#Function with input (parametrs)
def hello(name):
    print("Hai",name)
hello("Niya")

#Function that returns value
def hello(a,b):
    return a*b
n=hello(5,9)
print(n)

#Function with default value
def hello(name="User"):
    print("Hey",name)
hello()
hello("Niya")