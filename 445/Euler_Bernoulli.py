from __future__ import division, print_function
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 17:17:02 2016
Euler_Bernoulli Beam
This file contains the following programs:
E_B - creates the beam
E_B_cant - creates the cantilever beam
E_B_f - force on beam
E_B_f_additional - adds additional force to beam
@author: crhea
"""
import numpy as np
##Create the A matrix
## This will make our Euler Bernoulli beam Matrix based off the values in our book!
def E_B(n):
    A = np.zeros((n,n))
    count = 0
    for i in [12,-6,4/3]:
        A[0,0+count] = i 
        count += 1 
    count = 0
    for j in range(1,len(A)-2): 
        count = 0
        for i in [1,-4,6,-4,1]:
            A[j,j+count-2] = i
            count += 1
    count = 0
    for i in [-4,6,-4,1]:
        A[n-2,n-1-count] = i
        count += 1
    count = 0
    for i in [4/3,-6,12]:
        A[n-1,n-1-count] = i
        count += 1
    return A
    

def E_B_cant(n):
    A = np.zeros((n,n))
    count = 0
    for i in [12,-6,4/3]:
        A[0,0+count] = i 
        count += 1 
    count = 0
    for j in range(1,len(A)-2): 
        count = 0
        for i in [1,-4,6,-4,1]:
            A[j,j+count-2] = i
            count += 1
    count = 0
    for i in [-43/25,111/25,-93/25,1]:
        A[n-2,n-1-count] = i
        count += 1
    count = 0
    for i in [12/25,24/25,12/25]:
        A[n-1,n-1-count] = i
        count += 1
    return A

## And now I am making each beam a class for funsies

class Beam:
    def __init__(self,Beam_type,start,end,n_val):
        self.type = Beam_type
        self.start = start
        self.end = end
        self.n_val = n_val
    def matrix(self):
        if self.type == 'Regular':
            Matrix_Beam_type = E_B(self.n_val)    
        elif self.type == 'Cantilever': 
            Matrix_Beam_type = E_B_cant(self.n_val)
        elif self.type != 'Regular' and self.type != 'Cantilever': 
            print("Please enter either 'Regular' or 'Cantilever'")
        return Matrix_Beam_type

## This is just the righthand side of the EB differential equation
    
def E_B_f(E,I,w,d,L,n):
    g = 9.81
    h = L/n
    f = np.ones((n,1))
    f = (h**4/(E*I(w,d)))*f
    for i in range(0,n):
        f[i,0] = f[i,0]*(-480*w*d*g)
    return f

## And now what if i want to add ANY weight
## Add is a function for the additional weight
def E_B_f_additional(E,I,w,d,L,n,Add,add_start,add_end):
    g = 9.81
    h = L/n
    f = np.ones((n,1))
    f = (h**4/(E*I(w,d)))*f
    for i in range(0,n):
        f[i,0] = f[i,0]*(-480*w*d*g)
    ##Now lets deal with the additional error. Note add_start and end will be
    ##given as a distances from the start so we need to fix that...
    ## This checks if length is an integer, if it isnt then we make it an integer... We add one because int() rounds down! length is simply mapping the weight region from the terms of meters (or cm or whatever) to the partitioned form...
    length  = (add_end-add_start)*(n/L)
    if isinstance(length,int):
        length = length
    else: length = int(length)+1
    for k in range(0,length):
        f[add_start*(n/L)+k,0] = f[add_start*(n/L)+k,0] + Add(k)
    return f
