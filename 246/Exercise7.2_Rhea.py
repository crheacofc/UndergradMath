# -*- coding: utf-8 -*-
"""
Carter Rhea
October 22, 2015
Exercise 7.2
"""
from warnings import warn
from math import sin, cos
def newton(f, Df, x0, error_tolerance, maximum_steps):
    x = x0
    for step in range(maximum_steps):
        try:
            x_new = x - f(x)/Df(x)
            error_estimate = abs(x_new - x)
            x = x_new
            if error_estimate <= error_tolerance:
                # We are finished early
                return x, error_estimate
                
        except ZeroDivisionError:
            warn('Division by zero, this is the best i can do!')
            return x,error_estimate
            break

# Demonstration
#from math import cos, sin

def f(x): return x**2 + 1
def Df(x): return 2*x

def f2(x): return 2*sin(x)**2
def Df2(x): return 4*sin(x)*cos(x)


try:
    root, estimated_error = newton(f, Df, x0=1, error_tolerance=1e-10, 
                                   maximum_steps=100)
    print("The root is %.16g with %.2g error" %(root, estimated_error))
    
except TypeError as message:
    print("Sorry; that does not work. The derivative is 0")

try:
    root, estimated_error = newton(f2, Df2, x0=1, error_tolerance=1e-10, 
                                   maximum_steps=100)
    print("The root is %.16g with %.2g error" %(root, estimated_error))
    
except TypeError as message:
    print("Sorry; that does not work. The derivative is 0")
