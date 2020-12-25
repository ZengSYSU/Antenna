# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from mayavi import mlab
import math
import os

_path = os.getcwd()
os.chdir(_path)
gain = pd.read_csv('Gain Plot 1.csv')

Phi = gain.iloc[:, 0]
phi = Phi.astype(np.float)
for index in range(len(phi)):
    phi[index] = math.radians(phi[index])
Theta = gain.iloc[:, 1]
theta = Theta.astype(np.float)
for index in range(len(theta)):
    theta[index] = math.radians(theta[index])

dB_min = np.min(gain.iloc[:, 2])
scale = abs(dB_min) + 1
dB = gain.iloc[:, 2] + scale

r = np.multiply(dB, np.sin(theta))
x = np.multiply(r, np.cos(phi))
y = np.multiply(r, np.sin(phi))
z = np.multiply(dB, np.cos(theta))

mlab.plot3d(x, y, z, r, tube_radius=1, colormap="Spectral")
mlab.show()
