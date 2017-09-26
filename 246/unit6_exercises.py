
# -*- coding: utf-8 -*-
"""
Carter Rhea
October 10,2015
This program calculates both trapezoid rules, the midpoint rule, and simpson's rule 
and prints the value and error for different n values.
"""
#Import from integration module
from math import tan, cosh
from lab_6 import trapezoid1,trapezoid2,midpoint,simpson
def f(x): return 1/x**2
def g(x): return x**4 + tan(x) - cosh(x)**2
#Step through different n values
for el in [10,100,1000]:
    for fun in [f,g]:
        x = trapezoid1(f,1,3,el)
        err_x=2/3-x
        print("At %s steps for function  the estimate for the trapezoid1 rule is %s with error %9.2e"%(el,x,err_x))
        y = trapezoid2(f,1,3,el)
        err_y=2/3-y
        print("At %s steps for function %s the estimate for the trapezoid2 rule is %s with error %9.2e"%(el,fun,y,err_y))
        z = midpoint(f,1,3,el)
        err_z=2/3-z
        print("At %s steps for function %s the estimate for the midpoint rule is %s with error %9.2e"%(el,fun,z,err_z))
        w = simpson(f,1,3,el)
        err_w=2/3-w
        print("At %s steps for function %s the estimate for simposon's rule is %s with error %9.2e"%(el,fun,w,err_w))
        print()
