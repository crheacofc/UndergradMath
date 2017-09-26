# -*- coding: utf-8 -*-
"""
Carter Rhea
October 1
Revised to include iterations
"""

##Bisection Method!!
from math import sin
f = lambda x: 10-2*x+sin(x)
def bisection(f,a,b,its_max):
    c=(a+b)/2
    k=0
    val =[]
    i=0
    while (c-a>0) and (i<=its_max):
        if f(a)*f(c)<0:
            b=c
        else: a=c
        c=(b+a)/2
        err = abs(c-a)
        k+=1
        val.append([c,err,k])
        i+=1
    return val
    
def main():
    vals = bisection(f,0.,7.,100)
    for val in vals:
        print('The root is %s with an error of %s with %s function evaluations' %(val[0],val[1],val[2]))    
    
    
main()