"""
4. Write a python script to print greater between two numbers. Print number only once
even if the numbers are the same
"""
print("Enter Three Number")
num1 = int(input("Enter First Number "))
num2 = int(input("Enter Second Nmber"))
num3 = int(input("Enter Third Number"))

if num1 < num2 < num3:
    print(num1,"or", num2,"<",num3)
if num1 < num3 < num2:
    print(num1,"or", num3, "<",num2)
if num2 < num3 < num1:
    print(num3,"or", num2,"<",num1)

if num1 > num2 > num3:
    print(num1,"or", num2,">",num3)
if num1 > num3 > num2:
    print(num1,"or" ,num3, ">",num2)
if num2 > num3 > num1:
    print(num3,"or" ,num2,">",num1)
if num1 == num2 == num3:
    print("Given Number Is Equal")
    

    
