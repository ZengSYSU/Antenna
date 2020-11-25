# -*- coding: utf-8 -*-
import paraCalc
import wg
import sim

class Horn:
    def __init__(self, freq, HPE, HPH, wg_name=None):
        self.freq = freq
        self.HPE = HPE
        self.HPH = HPH
        self.wg_name = wg_name
        self.wg_a, self.wg_b, self.horn_a, self.horn_b, self.horn_l = None, None, None, None, None

    def wg_size(self):
        if self.wg_name is None:
            self.wg_a, self.wg_b = wg.check_by_freq(self.freq)
        else:
            self.wg_a, self.wg_b = wg.check_by_name(self.wg_name)
        return self.wg_a, self.wg_b

    def para(self):
        self.wg_size()
        if (self.wg_a or self.wg_b) is None:
            print('Input error!')
        else:
            self.horn_a, self.horn_b, self.horn_l = paraCalc.calc(self.freq, self.HPE, self.HPH, self.wg_a, self.wg_b)

    def realize_in_hfss(self):
        h = sim.HFSS()

        # 设置变量
        h.set_variable('wg_a', self.wg_a)
        h.set_variable('wg_b', self.wg_b)
        h.set_variable('wg_l', self.wg_a*1.5)
        h.set_variable('horn_a', self.horn_a)
        h.set_variable('horn_b', self.horn_b)
        h.set_variable('horn_l', self.horn_l)
        h.set_variable('wg_t', 0.5)
        h.set_variable('ab', 75/self.freq)

        # 波导内腔
        h.create_centered_rectangle('wg_a', 'wg_b', 0, 'wg_in')
        h.create_centered_rectangle('wg_a', 'wg_b', 'wg_l', 'wg_in_')
        h.connect('wg_in', 'wg_in_')

        # 喇叭内腔
        h.create_centered_rectangle('wg_a', 'wg_b', 'wg_l', 'horn_in')
        h.create_centered_rectangle('horn_a', 'horn_b', 'wg_l+horn_l', 'horn_in_')
        h.connect('horn_in', 'horn_in_')

        # 波导外形
        h.create_centered_rectangle('(wg_a+wg_t*2)', '(wg_b+wg_t*2)', '-wg_t', 'wg')
        h.create_centered_rectangle('(wg_a+wg_t*2)', '(wg_b+wg_t*2)', 'wg_l', 'wg_')
        h.connect('wg', 'wg_')

        # 喇叭外形
        h.create_centered_rectangle('(wg_a+wg_t*2)', '(wg_b+wg_t*2)', 'wg_l', 'horn')
        h.create_centered_rectangle('(horn_a+wg_t*2)', '(horn_b+wg_t*2)', 'horn_l+wg_l', 'horn_')
        h.connect('horn', 'horn_')

        # 布尔运算生成喇叭，然后设为PEC
        h.unite('horn', 'wg')
        h.unite('horn_in', 'wg_in')
        h.subtract('horn', 'horn_in')
        h.set_material('horn')

        # 生成区域并赋予辐射边界
        h.create_region('ab')
        h.assign_radiation_region()
        h.insert_radiation_setup()

        # 设置端口
        h.create_centered_rectangle('wg_a', 'wg_b', 0, 'port')
        h.assign_port('port')
        h.insert_analysis_setup(self.freq)

        # 创建报告
        h.create_reports()

        # 保存工程并运行
        h.save_prj()
        h.run()


if __name__ == '__main__':
    f, E, H = 10, 30, 20
    a_horn = Horn(f, E, H)
    a_horn.realize_in_hfss()
