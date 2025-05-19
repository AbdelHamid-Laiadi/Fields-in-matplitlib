# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 21:46:15 2023

@author: HAMID

This Python program reads renewable electricity generation data from a file (`germany-energy-sources.txt`),
 converts the values from gigawatt-hours to terawatt-hours, and creates a stacked bar chart showing
Germany’s renewable electricity production (from hydroelectric, wind, biomass, and photovoltaics) 
from 1990 to 2018. Each energy source is visually distinguished using different hatching patterns,
and the chart displays the total contribution of each source per year.

"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('germany-energy-sources.txt', skiprows=2, dtype='f8')
years = data[:,0]
n = len(years)

# GWh to TWh
data[:,1:] /= 1000

fig = plt.figure()
ax = fig.add_subplot(111)
sources = ('Hydroelectric', 'Wind', 'Biomass', 'Photovoltaics')
hatch = ['oo', '', 'xxxx', '//']
bottom = np.zeros(n)
bars = [None]*n
for i, source in enumerate(sources):
    bars[i] = ax.bar(years, bottom=bottom, height=data[:,i+1], color='w',
                    hatch=hatch[i], align='center', edgecolor='k')
    bottom += data[:,i+1]

ax.set_xticks(years)
plt.xticks(rotation=90)
ax.set_xlim(1989, 2019)
ax.set_ylabel('Renewable Electricity (TWh)')
ax.set_title('Renewable Electricity Generation in Germany, 1990-2018')
plt.legend(bars, sources, loc='best')
plt.show()