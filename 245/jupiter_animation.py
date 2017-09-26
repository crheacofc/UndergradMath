# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 14:34:12 2015

@author: crhea
"""

from pylab import *
import moviepy.editor as mp
from moviepy.video.io.bindings import mplfig_to_npimage
from Orbits import trapezium_orbit,trapstep,ydot_orbit_3d


# PARAMETERS OF THE CURVE AND THE GIF

jupiter = {'xp':-3.5023653,'xv':0.00565429,'yp':-3.8169847,'yv':-0.00412490,'zp':-1.5507963,'zv':-0.00190589,'m':0.000954786104043}

jupiter_traj,jupiter_quant = trapezium_orbit(ydot_orbit_3d,[jupiter['xp'],jupiter['xv'],jupiter['yp'],jupiter['yv'],jupiter['zp'],jupiter['zv']],jupiter['m'],0,100000,1000,3)



curve_latex = (r"$\left(\,\, \cos(80t) - \cos(t^3),\,\,\,"
              +r"\sin(t) -  \sin(80t)^3 \,\,\right)$")
### increase fps to increase number of steps
gif_name = "test.gif"
gif_duration = 1
gif_fps = 100



# PRECOMPUTE THE CURVE

t_min=0
t_max = 1000
number_of_points = 1000

# INITIALIZE THE FIGURE

fig, ax = subplots(1, figsize=(4,4), facecolor='white')
ax.axis("on")
ax.set_title("Orbit of Jupiter")
#ax.set_xlabel("Sharks in hundreds ")
#ax.set_ylabel("Turtles in hundreds")

line, = ax.plot(jupiter_traj[:,0], jupiter_traj[:,1])

# ANIMATE WITH MOVIEPY

def make_frame(t):
    index_max = int( (1.0*t/times[-1])*number_of_points)
    line.set_xdata(jupiter_traj[:index_max,0])
    line.set_ydata(jupiter_traj[:index_max,1])
    return mplfig_to_npimage(fig)

clip = mp.VideoClip(make_frame, duration=gif_duration)
clip = clip.fx( mp.vfx.freeze, t='end', freeze_duration=1)
clip.write_gif(gif_name, fps=gif_fps)