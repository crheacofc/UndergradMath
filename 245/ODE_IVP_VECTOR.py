# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:19:38 2015
Carter Rhea
This module contains the numerical methods for vector valued ODE

xdot is the general form of a system of ODE; THEY MUST BE ENTERED EXACTLY THIS WAY!!!!
y[:,0] -- y_1
y[:,1] -- y_2
And so on....
where teh z[x,x] = first order differentials!
"""

import numpy as np

def xdot(t,y):
    z = np.matrix(np.zeros((1,2)))
    z[0,0] = y[:,1]**2-2*y[:,0]
    z[0,1] = y[:,0]-y[:,1]-t*y[:,1]**2
    return z


##Euler method for vectors
def eulerstep(func,t_i,y,h):
    return y+func(t_i,y)*h
    
def euler_vector(func,y_init,a,b,n,eqn,verbose=False):
    y = np.matrix(np.zeros((n,eqn)))
    t_0 = a
    y[0,:] = y_init
    h = (b-a)/n
    t = np.array([a])
    for i in range(1,n):
        t_i = t_0 + i*h
        y[i,:] = eulerstep(func,t_i,y[i-1,:],h)
        t = np.append(t,t_i)
    if verbose:
        return y,t
    return y


## Improved Euler method for vectors


def eulerstep_imp(func,t,y,h):
    return y+(func(t,y)+func(t+h,y+h)+h*func(t,y))*h/2
def euler_imp_vector(func,y_init,a,b,n,eqn,verbose=True):
    y = np.matrix(np.zeros((n,eqn)))
    t_0 = a
    t = np.array([a])
    y[0,:] = y_init
    h = (b-a)/n
    for i in range(1,n):
        t_i = t_0 + i*h
        y[i,:] = eulerstep_imp(func,t_i,y[i-1,:],h)
        t = np.append(t,t_i)
    if verbose:
        return y,t
    return y



## RUNGE KUTTA METHOD FOR VECTORS
def Kutta_eqn(func,t_i,y_i,h):
    k = np.array(np.zeros((1,4)))
    k[0,0] = h*xdot(t_i,y_i)
    k[0,1] = h*xdot(t_i+h/2,y_i+k[0,0]/2)
    k[0,2] = h*xdot(t_i+h/2,y_i+k[0,1]/2)
    k[0,3] = h*xdot(t_i+h,y_i+k[0,2])
    return k[0,0]+2*k[0,1]+2*k[0,2]+k[0,3]
def Kutta_step(func,t,y,h):
    return  y + (1/6)*Kutta_eqn(func,t,y,h)
def Runge_Kutta_vector(func,y_init_vec,a,b,n,verbose=True):
    h = (b-a)/n
    y = np.matrix(np.zeros((n,2)))
    t_0 = a
    y[0,:]=y_init_vec
    t=np.array([a])
    for i in range(1,n):
        t_i = t_0+i*h
        y[i,:] = Kutta_step(func,t_i,y[i-1,:],h)
        t = np.append(t,t_i)
    if verbose:
        return y,t
    return y[i,:]
    
## Trapezium Method for Vectors
def trapstep(func,t,y,h):
    return y+(func(t,y)+func(t+h,y+h*func(t,y)))*h/2
def trapezium_vector(func,y_init,a,b,n,eqn,verbose=False):
    y = np.matrix(np.zeros((n,eqn)))
    t_0 = a
    t = np.array([a])
    y[0,:] = y_init
    h = (b-a)/n
    for i in range(1,n):
        t_i = t_0 + i*h
        y[i,:] = trapstep(func,t_i,y[i-1,:],h)
        t = np.append(t,t_i)
    if verbose:
        return y,t
    return y



 
