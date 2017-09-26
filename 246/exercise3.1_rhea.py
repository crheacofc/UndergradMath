# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:48:51 2015

@author: crhea
"""
## This program will take any user inputted values for a,b, and c from the quadratic equation
## and solve the quadratic
from math import sqrt


## This asks the user what values to use from the quadratic equation

print('I am going to ask for the a,b, and c from the quadratic equation (ax^2+bx+c).')
a = eval(input("Input coefficient 'a': "))
b = eval(input("Input coefficient 'b': "))
c = eval(input("Input coefficient 'c': "))
## now we solve for roots that are real and imaginary...
d = b**2 - 4 * a * c


#This will handle the real roots
if (a==0 and b==0):
    if c ==0:
        print('this is not a quadratic')
    else:
        print('This isnt even true!')
elif a !=0:
    if d >=0:
        root0 = (-b + sqrt(b**2 - 4 * a * c))/(2 * a)
        root1 = (-b - sqrt(b**2 - 4 * a * c))/(2 * a)
        print('The roots of the equation',a,'x^2 +',b,'x +',c,'are',root0,'and',root1)
#This will handle the imaginary roots    
    else:
        real = -b/(2*a)
        imaginary = sqrt(abs(d))/(2*a)
        root0 = real+imaginary*1j
        root1 = real-imaginary*1j
        print('The roots of the equation',a,'x^2 +',b,'x +',c,'are',root0,"and",root1)

elif a==0:
    root0 = -c/b
    print('The root of the equation is',root0)
elif a==0 and c==0 and b!=0:
    root0==0
    print('The root of the equation is',root0)

