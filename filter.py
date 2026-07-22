num=[1,3,5,6,8,4,6,0,7,9]
even=filter(lambda x:x%2==0,num)
print(list(even))
odd=filter(lambda x:x%2!=0,num)
print(list(odd))