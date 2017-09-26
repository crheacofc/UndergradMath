# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:07:15 2015

@author: crhea
"""
from numpy import linspace
def f(x): return 1/x**2
def trapezoid1(f,a,b,n):
    h=(b-a)/n
    T=0
    for i in range(1,n):
        x = a+i*h
        T = T + f(x)
    T_n = h*(f(a)/2+T+f(b)/2)
    return T_n
    
def trapezoid2(f,a,b,n):
    h=(b-a)/n
    x=linspace(a+h,b-h,n-1)
    s=sum(f(x))
    T_n = h*(f(a)/2+s+f(b)/2)
    return T_n
    
def midpoint(f,a,b,n):
    h=(b-a)/n    
    x_new = linspace(a+h/2,b-h/2,n)
    x_f = f(x_new)
    M_10 = h*sum(x_f)
    return M_10
   
def simpson(f,a,b,n):
    T_n=trapezoid2(f,a,b,n)
    M_n=midpoint(f,1,b,n)
    S_n=(T_n+2*M_n)/3
    return S_n
    

