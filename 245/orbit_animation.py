# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 09:59:21 2015

@author: crhea
"""

import numpy as np

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation



from Orbits import ydot_orbit_3d,trapezium_orbit, trapstep




# Choose random starting points, uniformly distributed from -15 to 15
jupiter = {'xp':-3.5023653,'xv':0.00565429,'yp':-3.8169847,'yv':-0.00412490,'zp':-1.5507963,'zv':-0.00190589,'m':0.000954786104043}
jupiter_traj = trapezium_orbit(ydot_orbit_3d,[jupiter['xp'],jupiter['xv'],jupiter['yp'],jupiter['yv'],jupiter['zp'],jupiter['zv']],jupiter['m'],0,100000,1000,3)
saturn = {'xp':9.0755314,'xv':0.00168318,'yp':-3.0458353,'yv':0.00483525,'zp':-1.6483708,'zv':0.00192462,'m':0.000285583733151}
uranus = {'xp':8.3101420,'xv':0.00354178,'yp':-16.2901086,'yv':0.00127102,'zp':-7.2521278,'zv':0.00055029,'m':0.0000437273164546}
neptune = {'xp':11.4707666,'xv':0.00288930,'yp':-25.7294829,'yv':0.00114527,'zp':-10.8169456,'zv':0.00039677,'m':0.0000517759138449}
pluto = {'xp':-15.5387357,'xv':0.00276725,'yp':-25.2225594,'yv':-0.00170702,'zp':-3.1902382,'zv':-0.00136504,'m':1/(1.3*10**(8))}
saturn_traj = trapezium_orbit(ydot_orbit_3d,[saturn['xp'],saturn['xv'],saturn['yp'],saturn['yv'],saturn['zp'],saturn['zv']],saturn['m'],0,100000,1000,3)
uranus_traj = trapezium_orbit(ydot_orbit_3d,[uranus['xp'],uranus['xv'],uranus['yp'],uranus['yv'],uranus['zp'],uranus['zv']],uranus['m'],0,100000,1000,3)
neptune_traj = trapezium_orbit(ydot_orbit_3d,[neptune['xp'],neptune['xv'],neptune['yp'],neptune['yv'],neptune['zp'],neptune['zv']],neptune['m'],0,1000000,1000,3)
pluto_traj = trapezium_orbit(ydot_orbit_3d,[pluto['xp'],pluto['xv'],pluto['yp'],pluto['yv'],pluto['zp'],pluto['zv']],pluto['m'],0,100000,1000,3)

#for planet, in [[jupiter_traj],[saturn_traj],[uranus_traj],[neptune_traj],[pluto_traj]]:
#    x_t = np.array([planet[:,0],planet[:,2],planet[:,4]])
x_t = np.matrix(np.zeros((1000,3)))
x_t[:,0] = np.array(jupiter_traj[:,0])
x_t[:,1] = np.array(jupiter_traj[:,2])
x_t[:,2] = np.array(jupiter_traj[:,4])

# Set up figure & 3D axis for anim]ation
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1], projection='3d')
ax.axis('off')

# choose a different color for each trajectory
colors = plt.cm.jet(np.linspace(0, 1, 1))

# set up lines and points
lines = sum([ax.plot([], [], [], '-', c=c)
             for c in colors], [])
pts = sum([ax.plot([], [], [], 'o', c=c)
           for c in colors], [])

# prepare the axes limits
ax.set_xlim((-25, 25))
ax.set_ylim((-35, 35))
ax.set_zlim((5, 55))

# set point-of-view: specified by (altitude degrees, azimuth degrees)
ax.view_init(30, 0)

# initialization function: plot the background of each frame
def init():
    for line, pt in zip(lines, pts):
        line.set_data([], [])
        line.set_3d_properties([])

        pt.set_data([], [])
        pt.set_3d_properties([])
    return lines + pts

# animation function.  This will be called sequentially with the frame number
i=0
def animate(i):
    # we'll step two time-steps per frame.  This leads to nice results.
    i = 2*i

    for line, pt, xt in zip(lines, pts, x_t):
        x, y, z = x_t[i,0],x_t[i,1],x_t[i,2]
        line.set_data(x, y)
        line.set_3d_properties(z)

        pt.set_data(x, y)
        pt.set_3d_properties(z)

    ax.view_init(30, 0.3 * i)
    fig.canvas.draw()
    return lines + pts

# instantiate the animator.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=500, interval=30, blit=True)

# Save as mp4. This requires mplayer or ffmpeg to be installed
#anim.save('lorentz_attractor.mp4', fps=15, extra_args=['-vcodec', 'libx264'])

#plt.show()
