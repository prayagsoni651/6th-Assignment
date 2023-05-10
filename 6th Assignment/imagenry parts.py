
# 8. Write a python script to check whether a given quadratic equation has two real &
#    distinct roots, real & equal roots or imaginary roots


# prompt the user to enter the coefficients of the quadratic equation
a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

# calculate the discriminant
discriminant = b**2 - 4*a*c

# check the value of the discriminant to determine the type of roots
if discriminant > 0:
    # calculate the two roots using the quadratic formula
    root1 = (-b + (discriminant)**0.5)/(2*a)
    root2 = (-b - (discriminant)**0.5)/(2*a)
    print("The quadratic equation has two real and distinct roots: ", root1, "and", root2)
elif discriminant == 0:
    # calculate the single root
    root = -b/(2*a)
    print("The quadratic equation has real and equal roots: ", root)
else:
    # calculate the real and imaginary parts of the complex roots
    real_part = -b/(2*a)
    imag_part = (-discriminant)**0.5/(2*a)
    print("The quadratic equation has imaginary roots: ", real_part, "+", imag_part, "i and ", real_part, "-", imag_part, "i")
