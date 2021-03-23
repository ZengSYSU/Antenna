# -*- coding: utf-8 -*-
import geatpy as ea
import numpy as np


class MyProblem(ea.Problem):  # 继承Problem父类
    def __init__(self):
        name = 'MyProblem'  # 初始化name（函数名称，可以随意设置）
        M = 2  # 初始化M（目标维数）[Gain > 15dBi/theta = 45deg]
        max_or_min = [-1, 1]  # 初始化max_or_min（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        Dim = 2  # 初始化Dim（决策变量维数）
        varTypes = [0, 0]  # 初始化varTypes（决策变量的类型，元素为0表示对应的变量是连续的；1表示是离散的）
        lb = [-1 * np.pi, 0]  # 决策变量下界
        ub = [np.pi, np.pi]  # 决策变量上界
        lb_in = [1] * Dim  # 决策变量下边界（0表示不包含该变量的下边界，1表示包含）
        ub_in = [1] * Dim  # 决策变量上边界（0表示不包含该变量的上边界，1表示包含）
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, max_or_min, Dim, varTypes, lb, ub, lb_in, ub_in)

    def aimFunc(self, pop):  # 目标函数
        # 得到决策变量矩阵
        epsilon = pop.Phen[:, 0]
        theta = pop.Phen[:, 1]
        psi = np.pi * np.cos(theta) + epsilon
        pop.ObjV = np.zeros((pop.Phen.shape[0], self.M))  # 计算目标函数值，赋值给pop种群对象的ObjV属性
        pop.ObjV[:, 0] = np.sin(psi * 4) / np.sin(psi * 0.5)
        pop.ObjV[:, 1] = abs(theta - 0.25 * np.pi)


if __name__ == '__main__':
    """===============================实例化问题对象============================"""
    problem = MyProblem()  # 生成问题对象
    """==================================种群设置==============================="""
    Encoding = 'RI'  # 编码方式
    NIND = 500  # 种群规模
    Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges, problem.borders,
                      [10] * len(problem.varTypes))  # 创建区域描述器
    population = ea.Population(Encoding, Field, NIND)  # 实例化种群对象（此时种群还没被初始化，仅仅是完成种群对象的实例化）
    """================================算法参数设置============================="""
    myAlgorithm = ea.moea_NSGA2_templet(problem, population)  # 实例化一个算法模板对象
    myAlgorithm.mutOper.Pm = 0.2  # 修改变异算子的变异概率
    myAlgorithm.recOper.XOVR = 0.9  # 修改交叉算子的交叉概率
    myAlgorithm.MAXGEN = 200  # 最大进化代数
    myAlgorithm.logTras = 1  # 设置每多少代记录日志，若设置成0则表示不记录日志
    myAlgorithm.verbose = True  # 设置是否打印输出日志信息
    myAlgorithm.drawing = 1  # 设置绘图方式（0：不绘图；1：绘制结果图；2：绘制目标空间过程动画；3：绘制决策空间过程动画）
    """==========================调用算法模板进行种群进化=========================
    调用run执行算法模板，得到帕累托最优解集NDSet以及最后一代种群。NDSet是一个种群类Population的对象。
    NDSet.ObjV为最优解个体的目标函数值；NDSet.Phen为对应的决策变量值。
    详见Population.py中关于种群类的定义。
    """
    [NDSet, population] = myAlgorithm.run()  # 执行算法模板，得到非支配种群以及最后一代种群
    NDSet.save()  # 把非支配种群的信息保存到文件中
    print('The number of evolution is: %s' % myAlgorithm.evalsNum)
    if NDSet.sizes != 0:
        print('The objective value of the best solution is: %s' % NDSet.ObjV[0][0], NDSet.ObjV[0][1])
    else:
        print('Did not find any feasible solution.')
