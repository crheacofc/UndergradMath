# -*- coding: utf-8 -*-
"""
Carter Rhea
October 22, 2015
Excercise 7.1
"""

from math import sqrt

print("Let's solve a quadratic equation a*x**2 + b*x + c = 0.")
are_we_done_yet = False
while not are_we_done_yet: 
    try:
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        discriminant = b**2 - 4*a*c
        root_of_discriminant = sqrt(discriminant)
        roots = ( (-b - root_of_discriminant)/(2*a),  (-b + root_of_discriminant)/(2*a))
        print("Success!")
        print("The roots are %g and %g" % roots)
        are_we_done_yet = True  # so we can exit the while loop
        
    except ZeroDivisionError as message:
        if b==0:
            print('This is not true!')
        else:
            root0 = -c/b
            print('The root of the equation is',root0)
        are_we_done_yet = True
        
    except ValueError as domain_error:  #Domain issue so we have imaginary numbers
        if str(domain_error) == "math domain error":
            real = -b/(2*a)
            imaginary = sqrt(abs(discriminant))/(2*a)
            root0 = real+imaginary*1j
            root1 = real-imaginary*1j
            print('The roots of the equation',a,'x^2 +',b,'x +',c,'are',root0,"and",root1)
            are_we_done_yet = True
        else:
            print("Lets try to plug in an actual number this time...")
    except Exception as message:  # Any other exceptions
        print("Some exception that I have not planned for, with message:", message)
        print("Please try again.")  


print('\nThank you; please come again soon!')
