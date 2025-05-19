# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:57:41 2023

@author: HAMID

This Python program generates a **quiver plot** using Matplotlib, where arrows represent
a simple 2D vector field based on meshgrid coordinates from -10 to 10. Each arrow points
from the origin of its grid cell in the direction defined by the grid itself 
(i.e., the arrow at point $(x, y)$ points in the direction $(x, y)$).


"""

import matplotlib.pyplot as plt
import numpy as np

X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V)
ax.quiverkey(q, X=0.3, Y=1.1, U=10,
             label='Quiver key, length = 10', labelpos='E')

plt.show()