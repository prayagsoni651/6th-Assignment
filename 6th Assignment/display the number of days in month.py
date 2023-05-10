
#  11. Write a python script to take the month value in numeric format and display the
#      number of days in it.


month = int(input("Enter the month (in numeric format): "))

if month == 2:
    print("The month of February has 28 or 29 days.")
elif month in [4, 6, 9, 11]:
    print("The month has 30 days.")
else:
    print("The month has 31 days.")
