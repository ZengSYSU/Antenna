# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import math
from mayavi import mlab
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

phi, theta = np.meshgrid(phi, theta)
r = 1 * np.sin(theta)
x = r * np.cos(phi)
y = r * np.sin(phi)
z = 1 * np.cos(theta)

mlab.mesh(x, y, z)
mlab.show()
