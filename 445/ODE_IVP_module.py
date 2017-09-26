# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 11:37:45 2015
CARTER RHEA
MODULE FOR PROJECT ON ODE IVPs
"""
import numpy as np

##BASIC EULER
#This function will calculate the ODE IVP with euler method and then find the best approx. 
def euler(f,y_init,a,b,n):
    y = np.matrix(np.zeros((n,1)))
    y[0,0] = y_init
    h = (b-a)/n
    t_0=a
    for i in range(1,n):
        t_i = t_0+i*h
        y[i,0] = y[i-1,0] + f(t_i,y[i-1,0])*h
    
    return y
   

## RICHARDSON EXTRAPOLATION
# Basic RE on Euler
def richardson_extrapolation(f,y_init,a,b,n):
    E1 = euler(f,y_init,a,b,n)
    E2 = euler(f,y_init,a,b,2*n)
    err = ToL+1
    while err > ToL:    
        E1 = euler(f,y_init,a,b,n)
        E2 = euler(f,y_init,a,b,2*n)
        rich_ext = E2 + ((1/3.)*(E2-E1))
        err = abs((1/3.)*(E2-E2))
        n=2*n
    return rich_ext
    
## Improved Euler and once again checks for the best possible estimate
def improved_euler(f,y_init,a,b,n):
    y = np.matrix(np.zeros((n,1)))
    y[0,0] = y_init
    h = (b-a)/n
    t_0=a
    for i in range(1,n):
        t_i = t_0+i*h
        y[i,0] = y[i-1,0] + (f(t_i,y[i-1,0])+f(t_i+h,y[i-1,0]+h*f(t_i,y[i-1,0])))*h/2
    
    return y

## RUNGE KUTTA METHOD
def Runge_Kutta(f,y_init,a,b,n):
    h = (b-a)/n
    y = np.matrix(np.zeros((n,1)))
    y[0,0]=y_init
    t_0 = a
    for i in range(1,n):
        t_i = t_0 +i*h
        k1 = h*f(t_i,y[i-1,0])
        k2 = h*f(t_i+h/2,y[i-1,0]+k1/2)
        k3 = h*f(t_i+h/2,y[i-1,0]+k2/2)
        k4 = h*f(t_i+h,y[i-1,0]+k3)
        y[i,0] = y[i-1,0] + (1/6)*(k1+2*k2+2*k3+k4)
    return y
        
## Trapezoid

def trapezium(f,y_init,a,b,n):
    y = np.matrix(np.zeros((n,1)))
    y[0,0] = y_init
    h = (b-a)/n
    t_0=a
    for i in range(1,n):
        t_i = t_0+i*h
        y[i,0] = y[i-1,0] + (f(t_i,y[i-1,0])+f(t_i+h,y[i-1,0]+h*f(t_i,y[i-1,0])))*h/2

    return y
   
   
## Midpoint
def midpoint(f,y_init,a,b,n,ToL,verbose=False):
    y = np.matrix(np.zeros((n,1)))
    y[0,0] = y_init
    h = (b-a)/n
    t_0=a
    for i in range(1,n):
        t_i = t_0+i*h
        y[i,0] = y[i-1,0] + h*f(t_i+h/2,y+(h/2)*f(t_i,y[i-1,0]))

    return y
   
    