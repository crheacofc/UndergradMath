# -*- coding: utf-8 -*-
"""
Carter Rhea <crhea@g.cofc.edu>
"""
from numpy import linspace, sin, cos, pi
from matplotlib import pyplot as plt

x = linspace(-pi,pi)
plt.plot(x, sin(x),label="sine")
plt.plot(x, cos(x),label="cosine")
plt.legend()
plt.title("Sine and Cosine Graph")
plt.xlabel("X values from -pi to pi")
plt.ylabel("Y values from -1 to 1")
plt.grid()