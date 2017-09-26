# -*- coding: utf-8 -*-
"""
This module will hold all the tools required for project 1
"""
import numpy as np
from numpy import linspace

##Here is the function which calculates the value for the centered difference
def centered_diff(f,x_0,h):
    Df = (f(x_0+h)-f(x_0-h))/(2*h)
    return Df
    
## Forward Difference
def forward_diff(f,x_0,h):
    Df = (f(x_0+h)-f(x_0))/h
    return Df
## Backwards Difference
def backward_diff(f,x_0,h):
    Df = (f(x_0)-f(x_0-h))/h
    return Df
    


##This is the function for the trapezoid rule
def trapezoid2(f,a,b,n):
    h=(b-a)/n
    T=0
    for i in range(1,n):
        x = a+i*h
        T = T + f(x)
        T_n = h*(f(a)/2+T+f(b)/2)
    return T_n
    
## Other trap
def trapezoid(f,a,b,n):
    h=(b-a)/n
    x=linspace(a+h,b-h,n-1)
    s=sum(f(x))
    T_n = h*(f(a)/2+s+f(b)/2)
    return T_n
  
##Richardson Extrapolation
def richardson(f,x_0,h,ToL):
    #Calculate both values for the centered difference
    CD_n = centered_diff(f,x_0,h)
    CD_2n = centered_diff(f,x_0,2*h)
    err = ToL+1
    while err > ToL:    
        CD_n = centered_diff(f,x_0,h)
        CD_2n = centered_diff(f,x_0,2*h)
        rich_ext = CD_2n + ((1/3.)*(CD_2n-CD_n))
        err = abs((1/3.)*(CD_2n-CD_n))
        h=h/2
    return [rich_ext,err]
    
#Trapezoid recursive    
def trap_recursive(f,a,b,nmax,ToL):
    T_n=((f(a)+f(b))/2)*(b-a)
    n=1
    for steps in range(1,nmax):
        M_n = midpoint(f,a,b,2**(steps-1))
        T_2n = (T_n+M_n)/2
        err = ToL+1
        if err < ToL:
            break
        n = 2*n
        T_n=T_2n
        err = abs(T_2n-T_n)/3
    f_evals = 2**steps+1
    return T_2n,f_evals,err
    
#Modified Trapezoid
def mod_trap(f,a,b,n,h,ToL):
    T_n= trapezoid(f,a,b,n)
    CD_a = forward_diff(f,a,h)
    CD_b = backward_diff(f,b,h)
    T_mod = T_n - ((CD_b-CD_a)*h**2)/12
    T_n2= trapezoid(f,a,b,2*n)
    T_mod2 = T_n2 - ((CD_b-CD_a)*h**2)/12
    error = ToL+10
    while error>ToL:
        T_n= trapezoid(f,a,b,n)
        T_mod = T_n - ((CD_b-CD_a)*h**2)/12
        T_n2= trapezoid(f,a,b,2*n)
        T_mod2 = T_n2 - ((CD_b-CD_a)*h**2)/12 
        n=2*n
        error = abs(T_mod2-T_mod)
    return T_mod2,error
    
##Midpoint Rule
def midpoint(f,a,b,n):
    h=(b-a)/n    
    x_new = linspace(a+h/2,b-h/2,n)
    x_f = f(x_new)
    M = h*sum(x_f)
    return M
       
    
##Romberg
def Romberg(f,a,b,jmax,ToL,verbose=False):
    R=np.zeros((jmax,jmax))
    R[0,0] = (f(a)+f(b))*(b-a)/2
    for j in range(1,jmax):
        R[j,0] =(R[j-1,0]+midpoint(f,a,b,2**(j-1)))/2
        for k in range(1,j):
            R[j,k]=(4**k*R[j,k-1]-R[j-1,k-1])/(4**k-1)
            err = abs((R[j,k-1]-R[j-1,k-1])/(4**k-1))
            if err < ToL:
                break
    if verbose:
        print(R)
    f_eval = 2**j+1
    return R[j,k],err,f_eval
            
            

