# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:38:10 2015

@author: crhea
"""

from math import *
from numpy import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')


f = lambda t: 2*t
g = lambda t: 10 - 4.905*t
def plotfunc(f,g,a,b,n):
    t = linspace(a,b,n)
    y=[]
    z=[]
    for i in t:
        y.append(f(i))
        z.append(g(i))
    return t,y,z

def main(a,b,n):
    t,y,z = plotfunc(f,g,a,b,n) 
    ax.plot(t,y,z)
main(0,100,100)