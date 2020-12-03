# -*- coding: utf-8 -*-
import HFSSscript1130


class MicroStrip:
    def __init__(self, freq=None):
        self.freq = freq

    def call_hfss(self):
        h = HFSSscript1130.HFSS()

        h.set_variable('w', 16)
        h.set_variable('l', 32)
        h.set_variable('h', 0.8)
        h.set_variable('wd', 1.5)
        h.set_variable('l1', 12)
        h.set_variable('h1', 11)
        h.set_variable('w1', 3)
        h.set_variable('h2', 20)
        h.set_variable('h3', 4)

        # micro_strip
        h.create_rectangle('wd', 0, 'h', 'wd', 'l1', 'micro_strip', 'Z')
        h.create_rectangle('w', 0, 0, 'w', 'h1', 'ground', 'Z')
        h.create_rectangle('w', 'l1', 'h', 'w', 'h2', 'patch', 'Z')
        h.create_rectangle('w', 'l1', 'h', 'w1', 'h3', 'stair', 'Z')
        h.mirror('stair', 0, 'l1', 'h', 13, 0, 0)
        h.subtract('patch', 'stair')
        h.subtract('patch', 'stair_1')
        # Substrate
        h.create_box('w', 0, 0, 'w', 'l', 'h', 'Substrate')
        h.set_material('Substrate')
        # radiation
        h.create_region()
        h.assign_radiation_region()
        # Assign port&E
#        h.assign_perfecte()
        h.create_rectangle('wd', 0, 0, 'h', 'wd', 'port', 'Y')
        h.assign_port('port')
        # setup
        h.insert_setup(self.freq, 6)
        h.insert_sweep(2, 12)
        h.insert_field_setup()
        h.create_report()
        h.save()
        h.run()


if __name__ == '__main__':
    f = 3
    _micro = MicroStrip(f)
    _micro.call_hfss()
