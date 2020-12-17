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
freq.append(sp.iloc[0:, 0])
dB.append(sp.iloc[0:, 1])

plt.subplot(211)
plt.plot(freq, dB, color='red', marker='.', lw=5)
plt.xlabel('Freq[GHz]')
plt.ylabel('dB(S(1,1))')

theta, r, n = [], [], 180
theta.append((gain.iloc[0:, 0]))
r.append(gain.iloc[0:, 1])
# theta = np.arange(0, 2*np.pi, 2*np.pi / n)
print(r, theta)
ax = plt.subplot(212, projection='polar')
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_thetagrids(np.arange(0, 360, 30))
plt.plot(theta, r,  marker='.', color='black', lw=2)
plt.title('Pattern', fontsize=10)
plt.tight_layout()
plt.show()
