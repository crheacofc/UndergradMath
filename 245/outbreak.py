# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 11:34:38 2015

@author: crhea
"""
import numpy as np
from pylab import *
import moviepy.editor as mp
from moviepy.video.io.bindings import mplfig_to_npimage
from ODE_IVP_VECTOR import trapezium_vector
from matplotlib import pyplot as plt

# PARAMETERS OF THE CURVE AND THE GIF

a = 4.0
b = 0.25
r = 2.*10**(-3)
N = 1000
def ill(t,y):
    z = np.matrix(np.zeros((1,3)))
    z[0,0] = -r*y[:,1]*y[:,0]+b*y[:,2]
    z[0,1] = r*y[:,1]*y[:,0]-a*y[:,1]
    z[0,2] = a*y[:,1] - b*y[:,2]
    return z


def pop(t,y):
    z = np.matrix(np.zeros((1,2)))
    z[0,0] = -y[:,0]+y[:,0]*y[:,1]
    z[0,1] = y[:,1]-y[:,0]*y[:,1]
    #z[0,0] = -(1+f)*y[:,0]+y[:,0]*y[:,1]
    #z[0,1] = (1-f)*y[:,1]-y[:,0]*y[:,1]
    return z


curve_latex = (r"$\left(\,\, \cos(80t) - \cos(t^3),\,\,\,"
              +r"\sin(t) -  \sin(80t)^3 \,\,\right)$")
### increase fps to increase number of steps
gif_name = "test.gif"
gif_duration = 10
gif_fps = 50



# PRECOMPUTE THE CURVE
illness,time = trapezium_vector(ill,[50,100,0],0,7,1000,3,verbose=True)


population,time = trapezium_vector(pop,[.5,2],0,100,10000,2,verbose=True)

t_min=0
t_max = time[-1]
number_of_points = len(time)

# INITIALIZE THE FIGURE

fig, ax = plt.subplots(1, figsize=(4,4), facecolor='white')
ax.axis("on")
ax.set_title("Sharks vs. Sea Turtles")
ax.set_xlabel("Sharks in hundreds ")
ax.set_ylabel("Turtles in hundreds")
q
line, = ax.plot(population[:,0], population[:,1])

# ANIMATE WITH MOVIEPY

def make_frame(t):
    index_max = int( (1.0*t/time[-1])*number_of_points)
    line.set_xdata(population[:index_max,0])
    line.set_ydata(population[:index_max,1])
    return mplfig_to_npimage(fig)

clip = mp.VideoClip(make_frame, duration=gif_duration)
clip = clip.fx( mp.vfx.freeze, t='end', freeze_duration=1)
clip.write_gif(gif_name, fps=gif_fps)