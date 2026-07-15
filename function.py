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

#Even-Odd
def even(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
print(even(9))

#Reverse a String
def rev(text):
    return text[::-1]
print(rev("Niya"))

#Palindrome using function
def pal(text):
    reverse_text=text[::-1]
    if text==reverse_text:
        return "Palindrome"
    else:
        return "Not Palindrome"
print(pal("malayalam"))

#Factorial
def fact(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result
print(fact(4))