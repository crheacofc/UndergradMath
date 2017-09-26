# -*- coding: utf-8 -*-
"""
Carter Rhea
September 28
Revised to include iterations
"""

##Bisection Method!!
from scipy.special import ellipj, ellipk, ellipe
import scipy
from scipy import *


from math import sin
f = lambda x: 2*ellipe(x**2)-ellipk(x**2)
def bisection(f,a,b,ToL,MAXIT):
    c=(a+b)/2
    k=0
    val =[]
    while (c-a>=ToL) and (k<=MAXIT):
        if f(a)*f(c)<0:
            b=c
        else: a=c
        c=(b+a)/2
        err = abs(c-a)
        k+=1
        val.append([c,err,k])
    return val
    
def main():
    for j in [10**(-8),0]:
        vals = bisection(f,0.,1.,j,100)
        for val in vals:
            print('The root is %s with an error of %s with %s function evaluations' %(val[0],val[1],2*val[2]))    
        
    
main()