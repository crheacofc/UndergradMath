# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:49:06 2015
Centered Difference Formula
@author: crhea
"""
import numpy
from math import sin, pi
from Project1_module_rhea import centered_diff,trap_recursive,trapezoid2,richardson,mod_trap,Romberg
f = lambda x: x**3 + 2*x**2 + 8
g = lambda x: numpy.log(x**2)
k = lambda x: numpy.sin(x)
x_0=2
h=.01
ToL = 10e-8
a=1
b=3
n=10
def main():
    #x_0=eval(input('Please input x_0:  '))
    #h=eval(input('Please input h:  '))
    Df = centered_diff(f,x_0,h)
    print("The calculated derivative using centered difference is %s"%(Df))
    R_E,error = richardson(f,x_0,h,ToL)
    print("The calculated derivative using Richard's extrapolation is %s with an error of %s"%(R_E,error))
    Trap = trapezoid2(f,a,b,n)
    print("The calculated integral value using the trapezoid rule is %s"%(Trap))
    #R_T = trap_recursive(f,a,b,n,ToL)
    #print("The calculated integral value using the recursive trapezoid rule is %s"%(R_T))    
    T_mod,error = mod_trap(k,0,2*pi,n,h,ToL)
    print("The calculated integral value using the modified trapezoid rule is %s with an error estimate of %s."%(T_mod,error))
    Rom = Romberg(f,a,b,n,ToL)
    print("The integral value according to the Romberg method is %s with an error of %s " %(Rom[0],Rom[1]))
main()
print(Romberg(g,a,b,5,ToL,verbose=True))