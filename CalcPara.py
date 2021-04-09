# -*- coding: utf-8 -*-


def size(freq):
    # hp 馈源位置 h 尾杆高度 xf 离中心点位置 d 点源间距
    l, w, h, xf, d = None, None, None, None, None
    hp = [0, 0, 0, 0, 0, 0, 0, 0]
    if freq >= 0:
        # l, w, xf = 54.4, 52.9, 15  # d = l + d
        l, w, xf = 56.7, 53.2, 17.5
        d = (300/freq) * 0.5
        for index in range(len(hp)):
            #  hp[index] = l / 2 - xf + (index + 1) * round(d, 3)
            #  hp[index] = round(hp[index], 3)
            hp[index] = w/2.0 + (index + 1) * round(d, 3)
        #  h = round((hp[7] + round(d, 3) + 0.5 * l + xf), 3)
        h = round(hp[7] + round(d, 3) + w/2.0)
    return l, w, h, hp, round(d, 3), xf


if __name__ == '__main__':
    _l, _w, _h, _hp, _d, _xf = size(2.44)
    print(_l, _w, _h, _hp, _d, _xf)
