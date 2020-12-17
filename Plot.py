# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import os

_path = os.getcwd()
os.chdir(_path)

sp = pd.read_csv('S Parameter Plot 1.csv')
gain = pd.read_csv('Gain Plot 2.csv')
freq, dB = [], []
freq.append(sp.iloc[:, 0])
dB.append(sp.iloc[:, 1])

plt.subplot(211)
plt.plot(freq, dB, color='red', marker='.', lw=5)
plt.xlabel('Freq[GHz]')
plt.ylabel('dB(S(1,1))')

theta, E = [], []
theta.append((gain.iloc[0:, 0]))
for index in range(len(theta)):
    theta[index] = theta[index]*np.pi/180
E.append(gain.iloc[0:, 1])
print(theta, E)

ax = plt.subplot(212, projection='polar')
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_thetagrids(np.arange(0, 360, 30))
plt.polar(theta, E,  marker='.', color='black', lw=2)

plt.title('Pattern', fontsize=10)
plt.tight_layout()
plt.show()
