# 7. Write a python script to check whether a given number is positive, negative or zero.

num = int(input("Enter a Number"))
if num==0:
    print("Given Number Is a Zero")
    print(type(num))
if num>0:
    print("Given Number Is a Positive Number")
    print(type(num))
else:
    print("Given Number Is Negative")
    