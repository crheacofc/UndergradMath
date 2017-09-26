# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 11:37:45 2015
CARTER RHEA
MODULE FOR PROJECT ON ODE IVPs
"""
import numpy as np

##BASIC EULER
#This function will calculate the ODE IVP with euler method and then find the best approx. 
def euler(f,y_init,a,b,n,ToL,verbose=False):
    y = np.matrix(np.zeros((n,1)))
    y[0,0] = y_init
    h = (b-a)/n
    t_0=a
    for i in range(0,n):
        t_i = t_0+i*h
        y[i,0] = y[i-1,0] + f(t_i,y[i-1,0])*h
    
    n=2*n
    err = ToL+1
    while err > ToL:
        h = (b-a)/n
        y1 = np.matrix(np.zeros((n,1)))
        y1[0,0] = y_init
        t = np.array([a])
        for i in range(1,n):
            t_i = t_0+i*h
            y1[i,0] = y1[i-1,0] + f(t_i,y1[i-1,0])*h
            t = np.append(t,t_i)
        err = abs(y1[-1,0] - y[-1,0])
        y=y1
        n=2*n
        if verbose:
            return y,t
    return y[-1,0]
   

## RICHARDSON EXTRAPOLATION
# Basic RE on Euler
def richardson_extrapolation(f,y_init,a,b,n,ToL):
    E1 = euler(f,y_init,a,b,n,ToL)
    E2 = euler(f,y_init,a,b,2*n,ToL)
    err = ToL+1
    while err > ToL:    
        E1 = euler(f,y_init,a,b,n,ToL)
        E2 = euler(f,y_init,a,b,2*n,ToL)
        rich_ext = E2 + ((1/3.)*(E2-E1))
        err = abs((1/3.)*(E2-E2))
        n=2*n
    return rich_ext
    
## Improved Euler and once again checks for the best possible estimate
def improved_euler(f,y_init,a,b,n,ToL,verbose=False):
    y = np.matrix(np.zeros((n,1)))
    y[0,0] = y_init
    h = (b-a)/n
    t_0=a
    for i in range(0,n):
        t_i = t_0+i*h
        y[i,0] = y[i-1,0] + (f(t_i,y[i-1,0])+f(t_i+h,y[i-1,0]+h*f(t_i,y[i-1,0])))*h/2
    
    n=2*n
    err = ToL+1
    while err > ToL:
        h = (b-a)/n
        y1 = np.matrix(np.zeros((n,1)))
        y1[0,0] = y_init
        t = np.array([a])
        for i in range(1,n):
            t_i = t_0+i*h
            y1[i,0] = y1[i-1,0] + (f(t_i,y1[i-1,0])+f(t_i+h,y1[i-1,0]+h*f(t_i,y1[i-1,0])))*h/2
            t = np.append(t,t_i)
        err = abs(y1[-1,0] - y[-1,0])
        y=y1
        n=2*n
        if verbose:
            return y,t
    return y[-1,0]

## RUNGE KUTTA METHOD
def Runge_Kutta(f,y_init,a,b,n,ToL):
    h = (b-a)/n
    y_i=y_init
    for i in range(1,n):
        t_i = a+i*h
        k1 = h*f(t_i,y_i)
        k2 = h*f(t_i+h/2,y_i+k1/2)
        k3 = h*f(t_i+h/2,y_i+k2/2)
        k4 = h*f(t_i+h,y_i+k3)
        y_1i = y_i +(1/6)*(k1+2*k2+2*k3+k4)
        print(y_1i)
        y_i=y_1i
        return y_1i
        
## Trapezoid

def trapezium(f,y_init,a,b,n,ToL,verbose=False):
    y = np.matrix(np.zeros((n,1)))
    y[0,0] = y_init
    h = (b-a)/n
    t_0=a
    for i in range(0,n):
        t_i = t_0+i*h
        y[i,0] = y[i-1,0] + (f(t_i,y[i-1,0])+f(t_i+h,y[i-1,0]+h*f(t_i,y[i-1,0])))*h/2
    
    n=2*n
    err = ToL+1
    while err > ToL:
        h = (b-a)/n
        y1 = np.matrix(np.zeros((n,1)))
        y1[0,0] = y_init
        t = np.array([a])
        for i in range(1,n):
            t_i = t_0+i*h
            y1[i,0] = y1[i-1,0] + (f(t_i,y1[i-1,0])+f(t_i+h,y1[i-1,0]+h*f(t_i,y1[i-1,0])))*h/2
            t = np.append(t,t_i)
        err = abs(y1[-1,0] - y[-1,0])
        y=y1
        n=2*n
        if verbose:
            return y,t
    return y[-1,0]
   
   
## Midpoint
def midpoint(f,y_init,a,b,n,ToL,verbose=False):
    y = np.matrix(np.zeros((n,1)))
    y[0,0] = y_init
    h = (b-a)/n
    t_0=a
    for i in range(0,n):
        t_i = t_0+i*h
        y[i,0] = y[i-1,0] + h*f(t_i+h/2,y+(h/2)*f(t_i,y[i-1,0]))
    
    n=2*n
    err = ToL+1
    while err > ToL:
        h = (b-a)/n
        y1 = np.matrix(np.zeros((n,1)))
        y1[0,0] = y_init
        t = np.array([a])
        for i in range(1,n):
            t_i = t_0+i*h
            y1[i,0] = y1[i-1,0] + h*f(t_i+h/2,(1/2)*f(t_i,y1[i-1,0]))
            t = np.append(t,t_i)
        err = abs(y1[-1,0] - y[-1,0])
        y=y1
        n=2*n
        if verbose:
            return y,t
    return y[-1,0]
   
    