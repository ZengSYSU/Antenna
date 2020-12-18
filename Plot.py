# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import os

_path = os.getcwd()
os.chdir(_path)

sp = pd.read_csv('S Parameter Plot 1.csv')
gain = pd.read_csv('Gain Plot 2.csv')
_gain = pd.read_csv('Gain Plot 3.csv')
freq, dB = [], []
freq.append(sp.iloc[:, 0])
dB.append(sp.iloc[:, 1])

plt.subplot(411)
plt.plot(freq, dB, color='red', marker='.', lw=5)
plt.xlabel('Freq[GHz]')
plt.ylabel('dB(S(1,1))')

theta, E, r = [], [], []
theta.append((gain.iloc[:, 0]))
for index in range(len(theta)):
    theta[index] = theta[index]*np.pi/180
E.append(gain.iloc[:, 1])
r.append(_gain.iloc[:, 1])

ax = plt.subplot(223, projection='polar')
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_thetagrids(np.arange(0, 360, 30))
plt.polar(theta, E,  marker='_', color='black', lw=2)
plt.title('Pattern', fontsize=10)

plt.subplot(224, projection='polar')
plt.polar(theta, r,  marker='_', color='green', lw=2)
plt.title('Pattern', fontsize=10)
# plt.tight_layout()
plt.show()
