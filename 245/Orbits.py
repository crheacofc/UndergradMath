# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 16:42:09 2015
Carter Rhea
This module contains all of my orbit calculations
"""
##Euler orbits

g = 2.95912208286*10**(-4) #gravitational constant
ms=1.00000597682 #mass of sun


import numpy as np
from math import sqrt

## 2 Dimensional one body
def ydot_orbit(t,x,m1):
    g = 2.95912208286*10**(-4) #gravitational constant
    ms=1.00000597682 #mass of sun    
    pxs = 0; pys = 0 #position of the sun
    px1=x[0,0];py1=x[0,2];vx1=x[0,1];vy1=x[0,3]
    dist = sqrt((pxs-px1)**2+(pys-py1)**2)
    z = np.array(np.zeros((1,4)))
    z[0,0] = vx1
    z[0,1] = (g*(ms+m1)*(pxs-px1))/(dist**3)
    z[0,2] = vy1
    z[0,3] = (g*(ms+m1)*(pys-py1))/(dist**3)
    return z
    
## 3 Dimenisonal one body
    
def ydot_orbit_3d(t,x,m1):
    pxs=0;pys=0;pzs=0 #position of sun
    px1=x[0,0];py1=x[0,2];pz1=x[0,4]
    vx1=x[0,1];vy1=x[0,3];vz1=x[0,5]  
    dist = sqrt((pxs-px1)**2+(pys-py1)**2+(pzs-pz1)**2)
    z = np.array(np.zeros((1,6)))
    z[0,0] = vx1
    z[0,1] = (g*(ms+m1)*(pxs-px1))/(dist**3)
    z[0,2] = vy1
    z[0,3] = (g*(ms+m1)*(pys-py1))/(dist**3)
    z[0,4] = vz1
    z[0,5] = (g*(ms+m1)*(pzs-pz1))/(dist**3)
    
    quant = np.array(np.zeros((1,4)))
    quant[0,0] = g*ms/dist
    quant[0,1] = m1*z[0,0]*z[0,1]
    quant[0,2] = m1*z[0,2]*z[0,3]
    quant[0,3] = m1*z[0,4]*z[0,5]

    return [z,quant]



##basic euler
def eulerstep_orbit(func,m1,t,x,h):
    return x+h*func(t,x,m1)
def orbit(func,ic,m1,a,b,n,dim):
    y = np.matrix(np.zeros((n,2*dim)))
    t_0 = a
    y[0,:] = ic
    h = (b-a)/n

    for i in range(1,n):
        t_i = t_0 + i*h
        y[i,:] = eulerstep_orbit(func,m1,t_i,y[i-1,:],h)

    return y


## This function will calculate the orbits of planets using Kepler's equations and eulers improved method. 
##a,b are the starting and endpoints respectively,
## ic is a vector of the initial conditions [x0,vx0,y0,yx0]
## n is the number of steps
## p is the steps per point
def eulerstep_imp_orbit(func,m,t,y,h):
    return y+(func(t,y,m)[0]+func(t+h,y+h*func(t,y,m)[0],m)[0])*h/2, func(t,y,m)[1]

def euler_improved_orbit(func,ic,m,a,b,n,dim):
    y = np.matrix(np.zeros((n,2*dim)))
    quantity = np.matrix(np.zeros((n,4)))
    t_0 = a
    y[0,:] = ic
    quantity[0,0] = (g*ms)/(((y[0,0])**2+(y[0,2])**2+(y[0,4])**2))**(3/2)
    h = (b-a)/n
    for i in range(1,n):
        t_i = t_0 + i*h
        y[i,:] = eulerstep_imp_orbit(func,m,t_i,y[i-1,:],h)[0]
        quantity[i,:] = trapstep(func,m,t_i,y[i-1,:],h)[1]
    return y,quantity
    
    
## Trapezium method for celestial mechanics. THis is different from the usual trap vector since it now has a mass to deal with
def trapstep(func,m1,t,y,h):
    return y+(func(t,y,m1)[0]+func(t+h,y+h*func(t,y,m1)[0],m1)[0])*h/2, func(t,y,m1)[1]

def trapezium_orbit(func,y_init,m1,a,b,n,dim):
    y = np.matrix(np.zeros((n,2*dim)))
    quantity = np.matrix(np.zeros((n,4)))
    t_0 = a
    y[0,:] = y_init
    quantity[0,0] = (g*ms)/(((y[0,0])**2+(y[0,2])**2+(y[0,4])**2))**(3/2)
    quantity[0,1] = m1*y[0,0]*y[0,1]
    quantity[0,2] = m1*y[0,2]*y[0,3]
    quantity[0,3] = m1*y[0,4]*y[0,5]
    h = (b-a)/n
    for i in range(1,n):
        t_i = t_0 + i*h
        y[i,:] = trapstep(func,m1,t_i,y[i-1,:],h)[0]
        ##finish puting the second part
        quantity[i,:] = trapstep(func,m1,t_i,y[i-1,:],h)[1]
    return y, quantity
    

    
 ## RUNGE KUTTA FOR CELESTIAL MECHANICS
def Kutta_eqn(func,t_i,y_i,m1,h):
    k1 = h*func(t_i,y_i,m1)[0]
    k2 = h*func(t_i+h/2,y_i+k1/2,m1)[0]
    k3 = h*func(t_i+h/2,y_i+k2/2,m1)[0]
    k4 = h*func(t_i+h,y_i+k3,m1)[0]
    k = k1+2*k2+2*k3+k4
    return k
def Kutta_step(func,t,y,m1,h):
    return  y + (1/6)*Kutta_eqn(func,t,y,m1,h),func(t,y,m1)[1]
def Runge_Kutta_orbit(func,ic,m1,a,b,n,dim):
    h = (b-a)/n
    y = np.matrix(np.zeros((n,2*dim)))
    quantity = np.matrix(np.zeros((n,4)))
    t_0 = a
    y[0,:] = ic
    quantity[0,0] = (g*ms)/(((y[0,0])**2+(y[0,2])**2+(y[0,4])**2))**(3/2)
    for i in range(1,n):
        t_i = t_0+i*h
        y[i,:] = Kutta_step(func,t_i,y[i-1,:],m1,h)[0]
        quantity[i,:] = trapstep(func,m1,t_i,y[i-1,:],h)[1]
    return y,quantity


## Midpoint

def midstep(func,m1,t,y,h):
    return y+h*(func(t+1/2,y+(h/2)*(func(t,y,m1)[0]),m1)[0]), func(t,y,m1)[1]

def midpoint_orbit(func,y_init,m1,a,b,n,dim):
    y = np.matrix(np.zeros((n,2*dim)))
    quantity = np.matrix(np.zeros((n,4)))
    t_0 = a
    y[0,:] = y_init
    quantity[0,0] = (g*ms)/(((y[0,0])**2+(y[0,2])**2+(y[0,4])**2))**(3/2)
    quantity[0,1] = m1*y[0,0]*y[0,1]
    quantity[0,2] = m1*y[0,2]*y[0,3]
    quantity[0,3] = m1*y[0,4]*y[0,5]
    h = (b-a)/n
    for i in range(1,n):
        t_i = t_0 + i*h
        y[i,:] = midstep(func,m1,t_i,y[i-1,:],h)[0]
        ##finish puting the second part
        quantity[i,:] = midstep(func,m1,t_i,y[i-1,:],h)[1]
    return y, quantity
    
