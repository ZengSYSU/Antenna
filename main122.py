# -*- coding: utf-8 -*-
import HFSSscript1130


class MicroStrip:
    def __init__(self, freq):
        self.freq = freq

    def call_hfss(self):
        h = HFSSscript1130.HFSS()

        # Substrate
        h.create_box(16, 0, 0, 16, 32, 0.8, "Substrate")
        h.set_material("Substrate", "FR4_epoxy")
        # micro_strip
        h.create_rectangle(1.5, 0, 0.8, 1.5, 12, "micro_strip", "Z")
        h.create_rectangle(16, 0, 0, 16, 11, "ground", "Z")
        h.create_rectangle(16, -24, 0.8, 16, 20, "patch", "Z")
        h.create_rectangle(16, -24, 0, 3, 4, "stair", "Z")
        h.create_rectangle(-16, -24, 0.8, -3, 4, "stair1", "Z")
        h.subtract("patch", "stair")
        h.subtract("patch", "stair1")
        # radiation
        h.create_region(25)
        h.assign_radiation_region()
        # Assign port
        h.create_rectangle(1.5, 0, 0, 0.8, 1.5, "port", "Y")
        h.assign_lumped("port", ["0mm", "0mm", "0mm"], ["0mm", "0mm", "0.8mm"])
        # setup
        h.insert_setup(self.freq, 6)
        h.insert_sweep(2, 12)
        h.insert_field_setup()
        h.create_report()
        h.save()
        h.run()
