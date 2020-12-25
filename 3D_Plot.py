# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from mayavi import mlab
import os

_path = os.getcwd()
os.chdir(_path)
gain = pd.read_csv('Gain Plot 1.csv')

Phi = gain.iloc[:, 0]
phi = Phi.astype(np.float)
Theta = gain.iloc[:, 1]
theta = Theta.astype(np.float)

dB_min = np.min(gain.iloc[:, 2])
scale = abs(dB_min) + 1
dB = gain.iloc[:, 2] + scale

phi, theta = np.meshgrid(phi, theta)
r = dB * np.sin(theta)
x = r * np.cos(phi)
y = r * np.sin(phi)
z = dB * np.cos(theta)

mlab.mesh(x, y, z)
mlab.show()
