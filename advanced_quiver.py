# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 14:00:33 2023

@author: HAMID

This Python program uses Matplotlib and NumPy to create a 
quiver plot—a grid of arrows—where each arrow's direction 
and magnitude represent a 2D vector field based on cosine 
and sine functions. The arrows are scaled relative to the 
plot's width, and a quiver key is added to indicate that 
an arrow length of 2 represents a velocity of 2 m/s.

"""

import matplotlib.pyplot as plt
import numpy as np

X, Y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))
U = np.cos(X)
V = np.sin(Y)

fig1, ax1 = plt.subplots()
ax1.set_title('Arrows scale with plot width, not view')
Q = ax1.quiver(X, Y, U, V, units='width')
qk = ax1.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')