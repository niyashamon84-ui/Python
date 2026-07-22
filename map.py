#Square of numbers
num=[1,2,3,4,5]
square=map(lambda x:x**2,num)
print(list(square))

#Cube of numbers
x=[3,6,8,10]
cube=map(lambda x:x**3,x)
print(list(cube))

#Add 2 list element wise
a=[1,2,3]
b=[7,5,4]
add=map(lambda a,b:a+b,a,b)
print(list(add))