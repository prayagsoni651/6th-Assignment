#  10. Write a python script to print greater among three numbers. Print number only once
#      even if the numbers are the same.


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2 and num1 > num3:
    print("The greatest number is:", num1)
elif num2 > num1 and num2 > num3:
    print("The greatest number is:", num2)
elif num3 > num1 and num3 > num2:
    print("The greatest number is:", num3)
else:
    print("The numbers are the same.")
