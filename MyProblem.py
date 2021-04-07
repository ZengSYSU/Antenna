# -*- coding: utf-8 -*-
import geatpy as ea
import numpy as np
import math
import Project
import pandas as pd


class MyProblem(ea.Problem):  # 继承Problem父类
    def __init__(self):
        name = 'MyProblem'  # 初始化name（函数名称，可以随意设置）
        M = 1  # 初始化M（目标维数）[Gain > 15dBi/theta = 45deg]
        max_or_min = [-1]  # 初始化max_or_min（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        Dim = 1  # 初始化Dim（决策变量维数）
        varTypes = [0]  # 初始化varTypes（决策变量的类型，元素为0表示对应的变量是连续的；1表示是离散的）
        lb = [-180]  # 决策变量下界
        ub = [180]  # 决策变量上界
        lb_in = [1] * Dim  # 决策变量下边界（0表示不包含该变量的下边界，1表示包含）
        ub_in = [1] * Dim  # 决策变量上边界（0表示不包含该变量的上边界，1表示包含）
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, max_or_min, Dim, varTypes, lb, ub, lb_in, ub_in)

    def aimFunc(self, pop):  # 目标函数
        # 得到决策变量矩阵
        epsilon = pop.Phen[:, 0]
        # theta = math.degrees(np.pi/4.0)
        pop.ObjV = np.zeros((pop.Phen.shape[0], self.M))  # 计算目标函数值，赋值给pop种群对象的ObjV属性
        print(epsilon)
        for index in range(pop.Phen.shape[0]):
            Project.Prj(0, epsilon[index], epsilon[index] * 2.0, epsilon[index] * 3.0, epsilon[index] * 4.0,
                        epsilon[index] * 5.0, epsilon[index] * 6.0, epsilon[index] * 7.0)
            Gain = pd.read_csv('Gain Plot 1.csv')
            dB_min = np.min(Gain.iloc[:, 2])
            scale = abs(dB_min) + 1
            dB = Gain.iloc[:, 2] + scale
            pop.ObjV[index] = dB[930]  # 30/492 45/711 60/930


if __name__ == '__main__':
    """===============================实例化问题对象============================"""
    problem = MyProblem()  # 生成问题对象
    """==================================种群设置==============================="""
    Encoding = 'RI'  # 编码方式
    NIND = 8  # 种群规模
    Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges, problem.borders)  # 创建区域描述器
    population = ea.Population(Encoding, Field, NIND)  # 实例化种群对象（此时种群还没被初始化，仅仅是完成种群对象的实例化）
    """================================算法参数设置============================="""
    myAlgorithm = ea.soea_SEGA_templet(problem, population)  # 实例化一个算法模板对象
    myAlgorithm.mutOper.Pm = 0.2  # 修改变异算子的变异概率
    myAlgorithm.recOper.XOVR = 0.9  # 修改交叉算子的交叉概率
    myAlgorithm.MAXGEN = 4  # 最大进化代数
    myAlgorithm.logTras = 0  # 设置每多少代记录日志，若设置成0则表示不记录日志
    myAlgorithm.verbose = True  # 设置是否打印输出日志信息
    myAlgorithm.drawing = 1  # 设置绘图方式（0：不绘图；1：绘制结果图；2：绘制目标空间过程动画；3：绘制决策空间过程动画）
    """==========================调用算法模板进行种群进化========================"""
    [BestIndi, population] = myAlgorithm.run()  # 执行算法模板，得到最优个体以及最后一代种群
    BestIndi.save()  # 把最优个体的信息保存到文件中
    """=================================输出结果=============================="""
    print('评价次数：%s' % myAlgorithm.evalsNum)
    print('时间已过 %s 秒' % myAlgorithm.passTime)
    if BestIndi.sizes != 0:
        print('最优的目标函数值为：%s' % BestIndi.ObjV[0][0])
        print('最优的控制变量值为：')
        for i in range(BestIndi.Phen.shape[1]):
            print(BestIndi.Phen[0, i])
    else:
        print('没找到可行解。')
