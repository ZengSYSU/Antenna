# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import os
import math

_path = os.getcwd()
os.chdir(_path)

sp = pd.read_csv('S Parameter Plot 1.csv')
gain = pd.read_csv('Gain Plot 2.csv')
_gain = pd.read_csv('Gain Plot 3.csv')
freq = sp.iloc[:, 0]
dB = sp.iloc[:, 1]

plt.subplot(411)
plt.plot(freq, dB, color='red', lw=5)
plt.xlabel('Freq[GHz]')
plt.ylabel('dB(S(1,1))')

theta = gain.iloc[:, 0]
for index in range(len(theta)):
    theta[index] = round(theta[index]*math.pi/180)
print(theta)
E = gain.iloc[:, 1]
r = _gain.iloc[:, 1]

ax = plt.subplot(223, projection='polar')
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_thetagrids(np.arange(0, 360, 30))
plt.polar(theta, E, color='black', lw=2)
plt.title('Pattern', fontsize=10)

plt.subplot(224, projection='polar')
plt.polar(theta, r, color='green', lw=2)
plt.title('Pattern', fontsize=10)
# plt.tight_layout()
plt.show()
