'''
12. Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part
'''

# Accept the complex number from the user
z = complex(input("Enter a complex number: "))

# Get the real and imaginary parts
real_part = z.real
imag_part = z.imag

# Compare the real and imaginary parts
if real_part > imag_part:
    print("The real part", real_part, "is greater than the imaginary part", imag_part)
elif imag_part > real_part:
    print("The imaginary part", imag_part, "is greater than the real part", real_part)
else:
    print("Both the real and imaginary parts are equal:", real_part)
