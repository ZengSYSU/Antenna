# -*- coding: utf-8 -*-
# import geatpy as ea

def size(freq):
    # hp 馈源位置 h 尾杆高度 xf 离中心点位置
    l, w, h, xf, d = None, None, None, None, None
    hp = [0, 0, 0, 0, 0, 0, 0, 0]
    if freq >= 0:
        l, w, xf = 54.4, 52.9, 15
        d = (300/freq) * 0.5
        h = 2 * l + round(d, 3)
        for index in range(len(hp)):
            hp[index] = h - l / 2 - xf + index * (round(d, 3) + l)
            hp[index] = round(hp[index], 3)
        h = round((hp[7] + 1.5 * l + round(d, 3) + xf), 3)

    return l, w, h, hp, round(d, 3), xf


if __name__ == '__main__':
    _l, _w, _h, _hp, _d, _xf = size(2.44)
    print(_l, _w, _h, _hp, _d, _xf)
