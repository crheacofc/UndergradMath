# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:19:38 2015
Carter Rhea
This module contains the numerical methods for vector valued ODE

xdot is the general form of a system of ODE; THEY MUST BE ENTERED EXACTLY THIS WAY!!!!
y[:,0] -- y_1
y[:,1] -- y_2
And so on....
where the z[x,x] = first order differentials!
"""

import numpy as np



def ydot(t_i,y,i):
    z = np.zeros(4)
    z[0] = y[:,1]
    z[1] = y[:,2]
    z[2] = y[:,3]
    z[3] = f(i)/(I(w,d)*E)
    return z

def Kutta_step(func,t,y,h,count):
    k1 = h*func(t,y,count)
    k2 = h*func(t+h/2.,y+k1/2.,count)
    k3 = h*func(t+h/2.,y+k2/2.,count)
    k4 = h*func(t+h,y+k3,count)
    k = k1+2*k2+2*k3+k4
    return  y + (1./6.)*k
def Runge_Kutta_vector(func,y_init_vec,a,b,n,verbose=True):
    h = (b-a)/n
    y = np.zeros((n,4))
    t_0 = a
    y[0,:]=y_init_vec
    t=np.array([a])
    for i in range(1,n):
        t_i = t_0+i*h
        y[i,:] = Kutta_step(func,t_i,y[i-1,:],h,i)
        t = np.append(t,t_i)
    if verbose:
        return y,t
    return y[i,:]




 
