
"""
粒子群算法
"""
import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import enum

def np_best_argextre():
    def argmin(a, axis=None, out=None):
        return np.argmin(a, axis, out)

    def argmax(a, axis=None, out=None):
        return np.argmax(a, axis, out)

    if PSO2.EXTREME == ExtremeEnum.MIN:
        return argmin
    else:
        return argmax


def np_best_extre():
    def min(a, axis=None, out=None, keepdims=np._NoValue, initial=np._NoValue):
        return np.min(a, axis, out, keepdims, initial)

    def max(a, axis=None, out=None, keepdims=np._NoValue, initial=np._NoValue):
        return np.max(a, axis, out, keepdims, initial)

    if PSO2.EXTREME == ExtremeEnum.MIN:
        return min
    else:
        return max


# def np_best_extreme():
#     def minimum(x1, x2, *args, **kwargs):
#         return np.minimum(x1, x2, *args, **kwargs)
#
#     def maximum(x1, x2, *args, **kwargs):
#         return np.maximum(x1, x2, *args, **kwargs)
#
#     if PSO2.EXTREME == ExtremeEnum.MIN:
#         return minimum
#     else:
#         return maximum


def np_worst_argextre():
    def argmin(a, axis=None, out=None):
        return np.argmin(a, axis, out)

    def argmax(a, axis=None, out=None):
        return np.argmax(a, axis, out)

    if PSO2.EXTREME == ExtremeEnum.MIN:
        return argmax
    else:
        return argmin


def np_worst_extre():
    def min(a, axis=None, out=None, keepdims=np._NoValue, initial=np._NoValue):
        return np.min(a, axis, out, keepdims, initial)

    def max(a, axis=None, out=None, keepdims=np._NoValue, initial=np._NoValue):
        return np.max(a, axis, out, keepdims, initial)

    if PSO2.EXTREME == ExtremeEnum.MIN:
        return max
    else:
        return min


def np_better():
    def less(x1, x2, *args, **kwargs):
        return np.less(x1, x2, *args, **kwargs)

    def greater(x1, x2, *args, **kwargs):
        return np.greater(x1, x2, *args, **kwargs)

    if PSO2.EXTREME == ExtremeEnum.MIN:
        return less
    else:
        return greater


def np_extreme():
    def maximum(x1, x2, *args, **kwargs):
        return np.maximum(x1, x2, *args, **kwargs)

    def minimum(x1, x2, *args, **kwargs):
        return np.minimum(x1, x2, *args, **kwargs)

    if PSO2.EXTREME == ExtremeEnum.MIN:
        return minimum
    else:
        return maximum


def math_better():
    def less(x1, x2):
        return x1 < x2;

    def greater(x1, x2):
        return x1 > x2

    if PSO2.EXTREME == ExtremeEnum.MIN:
        return lambda x1, x2: x1 <= x2
    else:
        return lambda x1, x2: x1 >= x2


def r():
    r = np.random.random()
    return r


# ExtremeEnum = enum.Enum('ExtremeEnum', ('MIN', 'MAX'))
class ExtremeEnum(enum.Enum):
    MIN = 0,
    MAX = 1


class PSO2(object):
    DIM = 2
    MIN = 0
    MAX = 1
    X_BOUND = [-5, 5]
    V_BOUND = [-1, 1]
    EXTREME = ExtremeEnum.MIN

    def formula(self, x):
        x1 = x[:, 0]
        x2 = x[:, 1]
        # x1 = 0.68678697;x2 =0.4749723;
        y = 20 + x1 ** 2 + x2 ** 2 - 10 * (np.cos(2 * np.pi * x1) + np.cos(2 * np.pi * x2))
        return y

    def __init__(self, population_size, max_gen_steps, extreme):
        # wv + c1 * r1 * (p_best - x) + c2 * r2 * (g_best - x)
        self.population_size = population_size
        self.max_gen_steps = max_gen_steps
        self.w = 1
        self.c1 = 1.49445
        self.c2 = 1.49445
        self.x = np.random.uniform(self.X_BOUND[PSO2.MIN], self.X_BOUND[PSO2.MAX], (self.population_size, self.DIM))
        self.v = np.random.uniform(self.V_BOUND[PSO2.MIN], self.V_BOUND[PSO2.MAX], (self.population_size, self.DIM))
        self.EXTREME = extreme;

    def next_v(self, r1, r2, c1, c2, p_best, g_best):
        w = self.w
        x = self.x
        v = self.v
        v2 = w * v + c1 * r1 * (p_best - x) + c2 * r2 * (g_best - x)
        return v2

    def handle_boundary_x(self, x):
        x[x > self.X_BOUND[PSO2.MAX]] = self.X_BOUND[PSO2.MAX]
        x[x < self.X_BOUND[PSO2.MIN]] = self.X_BOUND[PSO2.MIN]
        return x

    def handle_boundary_v(self, v):
        v[v > self.V_BOUND[PSO2.MAX]] = self.V_BOUND[PSO2.MAX]
        v[v < self.V_BOUND[PSO2.MIN]] = self.V_BOUND[PSO2.MIN]
        return v

    def evolve(self):
        fitness = self.formula(self.x)
        local = np_best_argextre()(fitness)
        self.p_best_x = self.x
        self.g_best_x = self.x[local]
        self.p_best_fitness = fitness
        self.g_best_fitness = fitness[local]

        log_best = []
        log_worst = []
        # 利用循环，也可以使用递归
        for step in range(self.max_gen_steps):
            self.x = self.x + self.v
            self.x = self.handle_boundary_x(self.x)
            self.v = self.next_v(r(), r(), self.c1, self.c2, self.p_best_x, self.g_best_x)
            self.v = self.handle_boundary_v(self.v)
            fitness = self.formula(self.x)


            # 本轮最优（整体 + 个体）
            better = np_better()(fitness, self.p_best_fitness)
            self.p_best_fitness[better] = fitness[better]
            self.p_best_x[better] = self.x[better]

            if math_better()(np_best_extre()(self.p_best_fitness), self.g_best_fitness):
                local = np_best_argextre()(self.p_best_fitness)
                self.g_best_fitness = self.p_best_fitness[local]
                self.g_best_x = self.p_best_x[local]

            # 本轮最差（整体）
            worse_local = np_worst_argextre()(self.p_best_fitness)
            g_worse_x = self.p_best_x[worse_local]
            g_worse_fitness = self.p_best_fitness[worse_local]
            log_worst.append('{0}轮整体最差解：x->{1}  fitness->{2}\n'.format(step, g_worse_x, g_worse_fitness))
            log_best.append('{0}轮整体最优解：x->{1}  fitness->{2}\n'.format(step, self.g_best_x, self.g_best_fitness))

            print('%s轮整体：最优x->%s  fitness->%s  最差x->%s  fitness->%s' % (step + 1, self.g_best_x, self.g_best_fitness, g_worse_x, g_worse_fitness))
            plt.clf()
            plt.scatter((self.p_best_x[:, 0] + self.p_best_x[:, 1]) / 2, self.p_best_fitness, s=20, color='k')
            plt.xlim(self.X_BOUND[PSO2.MIN], self.X_BOUND[PSO2.MAX])
            plt.ylim(self.X_BOUND[PSO2.MIN], self.X_BOUND[PSO2.MAX])
            plt.xlabel('(x1 + x2) / 2')
            plt.ylabel('fitness')
            plt.title('fitness curve')
            # plt.subplot(2, 1, 2)
            # plt.axes(projection='3d').scatter3D(self.p_best_x[:, 0], self.p_best_x[:, 1], self.p_best_fitness, c=self.p_best_fitness, cmap='Greens')
            plt.pause(0.02)
        # self.print_trace()
        # print(log_worst)
        # print(log_best)
        print()
        print('最终个体最优解：x->%s \n fitness->%s' % (self.p_best_x, self.p_best_fitness))
        plt.show()
        return

    def collect_trace(self, fitness):
        local = np_worst_argextre()(self.p_best_fitness)
        self.traceRecord.trace_record_worst_local = local
        self.traceRecord.trace_record_worst_fitness.append(self.p_best_fitness[local])
        self.traceRecord.trace_record_worst_x.append(self.p_best_x[local])


    def print_trace(self):
        table = []
        table.append(['No.', 'the worst local', 'the worst fitness', 'the worst x'])
        for i in range(len(self.traceRecord.trace_record_list)):
            # print('the worst x:%s'% self.traceRecord.trace_record_list)
            table.append([i+1,
                          self.traceRecord.trace_record_list[i][self.traceRecord.trace_record_worst_local],
                          # self.formula(self.traceRecord.trace_record_list[i])[self.traceRecord.trace_record_worst_local]
                          self.traceRecord.trace_record_worst_fitness[i],
                          self.traceRecord.trace_record_worst_x
                          ])
        print(table)

