# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt
import os

_path = os.getcwd()
os.chdir(_path)
sp = pd.read_csv('S Parameter Plot 1.csv')
print(sp)
print(sp.shape)
print(sp.columns)

df = pd.DataFrame(sp)
freq, dB = [], []
freq.append(df.iloc[1:, 0])
dB.append(df.iloc[1:, 1])

fig = plt.subplots()
plt.plot(freq, dB, color='red', marker='.', linewidth=5)
plt.xlabel('Freq[GHz]')
plt.ylabel('dB(S(1,1))')
plt.show()
