# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 22:42:56 2015
Carter Rhea
BASIC EULERS
""

def k(x,y):
    return x*y+x**3
n=10
a=0.0
y_init = 1
b=1.0
def eul(f,y_init,a,b,n):
    h=(b-a)/n
    t_0 = a
    y_i = y_init
    h=(b-a)/n
    for i in range(1,n):
        t_1 = t_0+i*h
        y_1 = y_i+f(t_1,y_i)*h
        y_i=y_1
    return t_1,y_1
val = eul(k,y_init,a,b,n)
print(val)