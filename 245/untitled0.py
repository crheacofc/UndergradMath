# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 18:54:24 2015

@author: crhea
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure, plot, semilogx, semilogy, loglog, title
from math import e, sqrt, floor

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



from Orbits import ydot_orbit, ydot_orbit_3d, trapezium_orbit, trapstep

jupiter = {'xp':-3.5023653,'xv':0.00565429,'yp':-3.8169847,'yv':-0.00412490,'zp':-1.5507963,'zv':-0.00190589,'m':0.000954786104043}
saturn = {'xp':9.0755314,'xv':0.00168318,'yp':-3.0458353,'yv':0.00483525,'zp':-1.6483708,'zv':0.00192462,'m':0.000285583733151}
uranus = {'xp':8.3101420,'xv':0.00354178,'yp':-16.2901086,'yv':0.00127102,'zp':-7.2521278,'zv':0.00055029,'m':0.0000437273164546}
neptune = {'xp':11.4707666,'xv':0.00354178,'yp':-25.7294829,'yv':0.00114527,'zp':-10.8169456,'zv':0.00039677,'m':0.0000517759138449}
pluto = {'xp':-15.5387357,'xv':0.00276725,'yp':-25.2225594,'yv':-0.00170702,'zp':-3.1902382,'zv':-0.00136504,'m':1/(1.3*10**(8))}

jupiter_traj = trapezium_orbit(ydot_orbit_3d,[jupiter['xp'],jupiter['xv'],jupiter['yp'],jupiter['yv'],jupiter['zp'],jupiter['zv']],jupiter['m'],0,100000,1000,3)
saturn_traj = trapezium_orbit(ydot_orbit_3d,[saturn['xp'],saturn['xv'],saturn['yp'],saturn['yv'],saturn['zp'],saturn['zv']],saturn['m'],0,100000,1000,3)
uranus_traj = trapezium_orbit(ydot_orbit_3d,[uranus['xp'],uranus['xv'],uranus['yp'],uranus['yv'],uranus['zp'],uranus['zv']],uranus['m'],0,100000,1000,3)
neptune_traj = trapezium_orbit(ydot_orbit_3d,[neptune['xp'],neptune['xv'],neptune['yp'],neptune['yv'],neptune['zp'],neptune['zv']],neptune['m'],0,1000000,1000,3)
pluto_traj = trapezium_orbit(ydot_orbit_3d,[pluto['xp'],pluto['xv'],pluto['yp'],pluto['yv'],pluto['zp'],pluto['zv']],pluto['m'],0,100000,1000,3)

fig = plt.figure()
ax = fig.gca(projection='3d')
for planet,color in [[jupiter_traj,'r'],[saturn_traj,'b'],[uranus_traj,'g'],[neptune_traj,'c'],[pluto_traj,'m']]:
     ax.plot_wireframe(np.array(planet[:,0]), np.array(planet[:,2]), np.array(planet[:,4]),color=color)
ax.scatter3D(0,0,0,marker="*",color="y")


ax.mouse_init(rotate_btn=1, zoom_btn=3)

plt.show()

