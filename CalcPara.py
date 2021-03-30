# -*- coding: utf-8 -*-
# import geatpy as ea
import numpy as np


def size(freq):
    # hp 馈源位置 h 尾杆高度 xf 离中心点位置 d 点源间距
    l, w, h, xf, d = None, None, None, None, None
    hp = [0, 0, 0, 0, 0, 0, 0, 0]
    if freq >= 0:
        # l, w, xf = 54.4, 52.9, 15  # d = l + d
        # l, w, xf = 54.416, 52, 8.576  # CalcPatch
        l, w, xf = 56, 46, 16
        d = (300/freq) * 0.5
        for index in range(len(hp)):
            hp[index] = l / 2 - xf + (index + 1) * round(d, 3)
            hp[index] = round(hp[index], 3)
        h = round((hp[7] + round(d, 3) + 0.5 * l + xf), 3)

    return l, w, h, hp, round(d, 3), xf


if __name__ == '__main__':
    _l, _w, _h, _hp, _d, _xf = size(2.44)
    print(_l, _w, _h, _hp, _d, _xf)
