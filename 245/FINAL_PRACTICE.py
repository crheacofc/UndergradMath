# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 11:38:18 2015
CARTER RHEA
PRACTICE CASES FOR ODE IVPs
"""
from ODE_IVP_module import euler,richardson_extrapolation,improved_euler,Runge_Kutta

def f(x,y): 
    return -x
y_init = 2
a = .25
b = .5
ToL = 10**(-2)
n=10

def main():
    e = euler(f,y_init,a,b,n,ToL)
    print(e)
    #r = richardson_extrapolation(f,y_init,a,b,n,ToL)
    #print(r)
    #v,t = improved_euler(f,y_init,a,b,n,ToL)
    #print(v)
    #print(t)
    #print(Runge_Kutta(f,y_init,a,b,n,ToL))
main()