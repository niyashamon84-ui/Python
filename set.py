set={10,20,100,90,70,50}
print(set) #prints the set randomly and not in the given order
#Common set operations
numbers={1,2,3}
print(numbers)
#add an element
#numbers.add(4)
print(numbers)
#Remove an element,it will show error if the given number is not in the set
numbers.remove(1)
print(numbers)
#Discard an element,it will not show error and just prints the original set,the example is given below
numbers.discard(5)
print(numbers)
#Remove random element
print(numbers.pop())
print(numbers)
#Union,denoted by | or .union()
set1={1,2,3}
set2={3,4,5}
print(set1|set2)
print(set1.union)
#Intersection,& or .intersection()
set3={1,2,3}
set4={2,3,4}
print(set3&set4)
print(set3.intersection(set4))
#Difference,- or .difference()
set3={1,2,3}
set4={2,3,4}
print(set3-set4)
print(set3.difference(set4))
#Symmetric Difference, ^ or .symmetric_difference()
set3={1,2,3}
set4={2,3,4}
print(set3^set4)
print(set3.symmetric_difference(set4))
#Length
print(len(numbers))