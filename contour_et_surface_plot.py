# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:07:16 2015

@author: crhea
"""
##3_d PLots for @ variable functions
from math import *
from numpy import *
from mpl_toolkits.mplot3d import axes3d 
import matplotlib.pyplot as plt
# Setup the 3D plot:
fig = plt.figure()
ax = fig.gca(projection='3d')

#define function of interest

def f(x,y):
    sin(x)**2+sin(y)**2
    
    
def plotfunc(f,a,b,n):
    x = linspace(-pi, pi, 30)
    y = linspace(-pi, pi, 30)
# Create Cartesian grid:
    X, Y = meshgrid(x, y)
    return X,Y
# Calculate values at grid points:
def main(a,b,n):
    X,Y = plotfunc(f,a,b,n)
    Z = sin(X)**2+sin(Y)**2 # Be sure to redefine Z as f!!!!
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1)
    
main(0,10,100)