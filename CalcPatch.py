import math
import numpy as np
from scipy import integrate

c = 3e11
freq = 10e9  # 2.44e9  # hz 工作频率
lambda0 = c / freq  # mm 真空波长

# 贴片宽度
er = 2.2  # 1.0006  # 介质相对介电常数， 空气
h = 1.588  # 5  # 介质板厚度
w = 0.5 * lambda0 * math.sqrt(2/(er + 1))  # 高于产生高次模场畸变，低于辐射效率降低

# 贴片长度
a = w / h
er_eff = 0.5 * (er + 1) + 0.5 * (er - 1) * math.pow((1 + 12/a), -0.5)  # 等效介电常数
lambda1 = lambda0 / math.sqrt(er_eff)  # 介质波长
delta_l = 0.412 * h * ((er_eff + 0.3) / (er_eff - 0.258)) * ((a + 0.264) / (a + 0.8))  # 边缘场等效伸长长度
length = 0.5 * lambda1 - 2 * delta_l

#  谐振输入电阻
k0 = 2 * np.pi / lambda0  # h/lambda0 <0.1
b = k0 * h


def func_G1(x):
    return 1/120/math.pow(math.pi, 2)*math.pow(math.sin(k0*w/2.0*math.cos(x))/math.cos(x), 2)*math.pow(math.sin(x), 3)


def func_G12(x):
    return 1/120/math.pow(math.pi, 2)*math.pow(math.sin(k0*w*math.cos(x)/2.0)/math.cos(x), 2)*np.i0(length*math.sin(x)*k0)*math.pow(math.sin(x), 3)


G1 = integrate.quad(func_G1, 0, np.pi)
G1 = G1[0]
G12 = integrate.quad(func_G12, 0, np.pi)
G12 = G12[0]
#G12 = 6.1683e-4
Rin0 = 0.5/(G1 + G12)
y0 = (length/np.pi) * np.arccos(math.sqrt(50/Rin0))
print(G1, G12, Rin0, length, w, y0)



