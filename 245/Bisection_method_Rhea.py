# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 13:12:18 2015
@author: crhea
"""

##Bisection Method!!
from math import sin
f = lambda x: 10-2*x+sin(x)
def bisection(f,a,b,ToL):
    c=(a+b)/2
    val =[]
    while (c-a>ToL):
        if f(a)*f(c)<0:
            b=c
        else: a=c
        c=(b+a)/2
        err = abs(c-a)
        val.append([c,err])
    return val
    
def main():
    vals = bisection(f,0.,7.,10**(-8))
    for val in vals:
        print('the roots are %s with an error of %s' %(val[0],val[1]))    
    
    
main()