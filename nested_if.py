x=int(input("Enter a number :"))
if x>0:
    print("Number is positive")
    if x%2==0:
        print("Number is even")
    else:
        print("Number is odd")
else:
    print("Number is zero or negative")