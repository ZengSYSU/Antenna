# -*- coding: utf-8 -*-
import math

#constant
t0, s0, a0, a1, a2 = 0.375, 0.25, 0.2974, 7.0401, -37.5383
c00,c01,c10, c11, c12, c13, c14, c15 = 44.8365, 4.3374, -8.1501, -2.9183, 8.4217, -13.2623, 10.6702, -3.4713
ah, bh, ch, dh, eh, fh, gh, hh, ih = 0.3534, -5.9711, -1.5379, 13.4735, 2.4359, -13.3102, -1.6386, 4.7981, 0.6333
ae, be, ce, de, ee, fe, ge, he = 0.1962, -11.3448, -1.9135, 41.7800, 5.7284, -47.9711, -4.8935, -6.4175
d0, d1, d2, d3, d4, d5, d6, d7, d8 = \
    0.1020, 2.9658e-2, -2.4894e-3, -2.0962e-2, 6.3027e-4, -5.9327e-6, -0.6802, -4.4039e-2, 1.0213e-3
f00, f01, f10, f11, f12, f13, f14, f15 = 44.3672, -4.098, -8.0775, -4.2683, 14.5647, -26.1244, 23.9791, -8.7301


def calc(freq, HPE, HPH, a, b):
    lam = 300 / freq
    k = HPH / HPE

    if k < 1:
        t = t0
        c0 = c00 + c01*math.log(k)
        c1 = c10 + c11*k + c12*k**2 + c13*k**3 + c14*k**4 + c15*k**5
        D = c0 + c1 * math.log(HPH)
        s = (a0 + a1 / k**2 + a2 / D) ** (-1)

        A = 0.5 * math.sqrt(
            (ah + ch*t**2 + eh*t**4 + gh*t**6 + ih*t**8) / (1 + bh*t**2 + dh*t**4 + fh*t**6 + hh*t**8)) * \
            lam * math.cos(HPH*math.pi/720) / math.tan(HPH*math.pi/720)

        B = 0.5 * math.sqrt(
            (ae + ce*s**2 + ee*s**4 + ge*s**6) / (1 + be*s**2 + de*s**4 + fe*s**6 + he*s**8)) * \
            lam * math.cos(HPE*math.pi/720) / math.tan(HPE*math.pi/720)

        R = A * (A - a) / (8 * lam * t)

    else:
        s = s0
        f0 = f00 + f01 * math.log(k)
        f1 = f10 + f11 / k + f12 / k**2 + f13 / k**3 + f14 / k**4 + f15 / k**5
        D = f0 + f1 * math.log(HPE)
        t = (d0 + d1*k + d2*k**2 + d3*D + d4*D**2 + d5*D**3) / (1 + d6*k + d7*D + d8*D**2)

        A = 0.5 * math.sqrt(
            (ah + ch * t ** 2 + eh * t ** 4 + gh * t ** 6 + ih * t ** 8) / (
                        1 + bh * t ** 2 + dh * t ** 4 + fh * t ** 6 + hh * t ** 8)) * \
            lam * math.cos(HPH*math.pi/720) / math.tan(HPH*math.pi/720)

        B = 0.5 * math.sqrt(
            (ae + ce * s ** 2 + ee * s ** 4 + ge * s ** 6) / (
                        1 + be * s ** 2 + de * s ** 4 + fe * s ** 6 + he * s ** 8)) * \
            lam * math.cos(HPE*math.pi/720) / math.tan(HPE*math.pi/720)

        R = B * (B - b) / (8 * lam * s)

    return round(A, 2), round(B, 2), round(R, 2), round(s, 4), round(t, 4)


if __name__ == '__main__':
    _A, _B, _R, _s, _t = calc(freq=8, HPE=9.89, HPH=12.62, a=35, b=17.5)
    print(_A, _B, _R, _s, _t)

