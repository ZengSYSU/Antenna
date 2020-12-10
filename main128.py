# -*- coding: utf-8 -*-
import ArrayScript


class Array:
    def __init__(self, freq, _ud, _vd):
        self.freq = freq
        self.ud = _ud
        self.vd = _vd
        self.num = [0, 0, 0, 0, 0, 0]

    def call_hfss(self):
        h = ArrayScript.HFSS()

        h.set_var('wg_a', 22.86)
        h.set_var('wg_b', 10.16)
        h.set_var('wg_z', 25.4)
        h.set_var('l', -1.27)
        h.set_var('a', 12.7)
        h.set_var('ud', self.ud)
        h.set_var('vd', self.vd)

        h.create_box(0, 0, 0, 'wg_b', 'wg_a', 'wg_z', 'WaveGuide')
        h.create_box('l', 'l', 'wg_z', 'a', 'wg_z', 'wg_z', 'AirBox')

        h.face_id()
        for index in range(len(self.num)):
            self.num[index] = h.face_id() + index
        print(self.num)
        h.assign_master(self.num[5], self.num[4])
        h.assign_slave(self.num[3], self.num[2], 0, 30)
        h.assign_fp()
        h.assign_wave_port()

        h.insert_setup(self.freq)
        h.insert_field_setup()
        h.array(25, 25, self.ud, self.vd)
        h.create_report()
        h.save()
        h.run()


if __name__ == '__main__':
    f, ud, vd = 9.25, 12.7, 25.4
    _array = Array(f, ud, vd)
    _array.call_hfss()
