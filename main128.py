# -*- coding: utf-8 -*-
import ArrayScript


class Array:
    def __init__(self, freq, _ud, _vd, wg_name=None, _id=None):
        self.freq = freq
        self.ud = _ud
        self.vd = _vd
        self.id = _id
        self.obj1 = 'WaveGuide'
        self.obj2 = 'Airbox'
        self.wg_name = wg_name
        self.wg_a, self.wg_b = 22.86, 10.16

    def call_hfss(self):
        h = ArrayScript.HFSS()

        h.set_var('wg_a', self.wg_a)
        h.set_var('wg_b', self.wg_b)
        h.set_var('idx', self.wg_b/2)
        h.set_var('idy', self.wg_a/2)
        h.set_var('wg_z', 25.4)
        h.set_var('l', -1.27)
        h.set_var('a', 12.7)
        h.set_var('ud', self.ud)
        h.set_var('vd', self.vd)

        h.create_box(0, 0, 0, 'wg_b', 'wg_a', 'wg_z', self.obj1)
        h.create_box('l', 'l', 'wg_z', 'a', 'wg_z', 'wg_z', self.obj2)
        h.face_id(self.obj1, 'idx', 'idy', 0)
        h.face_id(self.obj2, 'idx', 'idy', 'wg_z')
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
    f, ud, vd = 9.25, 12.7, 25.4
    _array = Array(f, ud, vd)
    _array.call_hfss()
