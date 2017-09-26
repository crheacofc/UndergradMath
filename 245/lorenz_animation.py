# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 15:16:58 2015

@author: crhea
"""

import numpy as np
from pylab import *
from matplotlib import pyplot as plt
import moviepy.editor as mp
from moviepy.video.io.bindings import mplfig_to_npimage
from ODE_IVP_VECTOR import trapezium_vector


# PARAMETERS OF THE CURVE AND THE GIF

def f(t,y):
    s=10
    r=28
    b=8/3
    z = np.matrix(np.zeros((1,3)))
    z[0,0] = s*(y[:,1]-y[:,0])
    z[0,1] = y[:,0]*(r-y[:,2])-y[:,1]
    z[0,2] = y[:,0]*y[:,1]-b*y[:,2]
    return z
n = 5000
lorenz = trapezium_vector(f,[5,5,5],0,50,n,3)




curve_latex = (r"$\left(\,\, \cos(80t) - \cos(t^3),\,\,\,"
              +r"\sin(t) -  \sin(80t)^3 \,\,\right)$")
### increase fps to increase number of steps
gif_name = "test.gif"
gif_duration = 1
gif_fps = 500



# PRECOMPUTE THE CURVE

t_min=0
t_max = n
number_of_points = n

# INITIALIZE THE FIGURE

fig, ax = plt.subplots(1, figsize=(4,4), facecolor='white')
ax.axis("on")
ax.set_title("Motion of Particle in air")
#ax.set_xlabel("Sharks in hundreds ")
#ax.set_ylabel("Turtles in hundreds")

line, = ax.plot(lorenz[:,0], lorenz[:,1])
# ANIMATE WITH MOVIEPY

def make_frame(t):
    index_max = int( (1.0*t/1)*number_of_points)
    line.set_xdata(lorenz[:index_max,0])
    line.set_ydata(lorenz[:index_max,1])
    return mplfig_to_npimage(fig)

clip = mp.VideoClip(make_frame, duration=gif_duration)
clip = clip.fx( mp.vfx.freeze, t='end', freeze_duration=1)
clip.write_gif(gif_name, fps=gif_fps)