# -*- coding: utf-8 -*-
import ArrayScript


class Array:
    def __init__(self, freq, _ud, _vd):
        self.freq = freq
        self.ud = _ud
        self.vd = _vd

    def call_hfss(self):
        h = ArrayScript.HFSS()

        h.set_var('wg_a', 0.9)
        h.set_var('wg_b', 0.4)
        h.set_var('wg_z', 1.0)
        h.set_var('l', -0.05)
        h.set_var('a', 0.5)
        h.set_var('b', 1)
        h.set_var('ud', self.ud)
        h.set_var('vd', self.vd)

        h.create_box(0, 0, 0, 'wg_b', 'wg_a', 'wg_z', 'WaveGuide')
        h.create_box('l', 'l', 'wg_z', 'a', 'b', 'wg_z', 'Airbox')
        h.assign_master()
        h.assign_slave(0, 30)
        h.assign_fp()
        h.assign_wave_port()
        h.insert_setup(self.freq)
        h.insert_field_setup()
        h.array(25, 25, self.ud, self.vd)
        h.create_report()
        h.save()
        h.run()


if __name__ == '__main__':
    f, ud, vd = 9.25, 0.5, 1.0
    _array = Array(f, ud, vd)
    _array.call_hfss()
