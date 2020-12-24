# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
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

x = dB * np.sin(theta) * np.cos(phi)
y = dB * np.sin(theta) * np.sin(phi)
z = dB * np.cos(theta)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(X**2 + Y**2)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, cmap='rainbow')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
