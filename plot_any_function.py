# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:44:51 2015

@author: crhea
"""
from math import *
from numpy import linspace, sin, cos, pi
from matplotlib import pyplot as plt
f = lambda x: e**(-x)
def plotfunc(f,a,b,n):
    x = linspace(a,b,n)
    y= []
    for i in x:
        y.append(f(i))
    return x,y

def main(a,b,n):
    x,y = plotfunc(f,a,b,n) 
    plt.plot(x,y)
    plt.grid()
main(-10*pi,10*pi,100)