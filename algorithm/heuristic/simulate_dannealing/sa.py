import numpy as np
import matplotlib.pyplot as plt
import math
import random

# Simulate Anneal
class SA(object):
    """
    退火
    """
    def fitness(self, x):
        y = x ** 3 - 60 * x ** 2 - 4 * x + 6
        return y

    def plot_baseline(self):
        x = np.arange(self.BOUND_X[0], self.BOUND_X[1], 1)
        y = self.fitness(x)
        plt.plot(x, y)

    def plot_vertical(self, x):
        vline = plt.axvline(x, self.BOUND_X[0], self.BOUND_X[1])
        return vline

    def next_t(self):
        # global _t
        self._t += 1
        return self.T_MAX / (1 + self._t)

    def __init__(self):
        self.wide=[-0.055, 0.055]
        self._t = 0                                 # time
        self.BOUND_X = [0, 100]
        self.x = np.random.uniform(low=self.BOUND_X[0], high=self.BOUND_X[1])
        self.y = self.fitness(self.x)           # initiate result
        self.T_MAX = 2000                           # maximum value of temperature
        self.T_MIN = 10                             # minimum value of temperature

    def evolve(self):
        best_x = None
        best_y = None
        t = self.T_MAX                              # initiate temperature
        plt.ion()
        self.plot_baseline()

        vline = None
        while t >= self.T_MIN:
            # generate a new x in the neighboorhood of x by transform function
            x_new = self.x + np.random.uniform(low=self.wide[0], high=self.wide[1]) * t
            if 0 <= x_new <= 100:
                y_new = self.fitness(x_new)
                # 如果取得更优解
                if y_new < self.y:
                    best_x = x_new
                    best_y = y_new
                    self.x = x_new
                    self.y = y_new
                # 如果非更优解，以一定概率转移
                # metropolis principle
                else:
                    p = math.exp(-(y_new - self.y) / t)
                    r = random.random()
                    # r = np.random.uniform(low=0, high=1)
                    if r < p:
                        self.x = x_new
                        self.y = y_new
            t = self.next_t()
            # plt.clf()
            if vline is not None:
                vline.remove()
            vline = self.plot_vertical(self.x)
            plt.pause(0.00001)
            print("t:%s x:%s y:%s" % (self._t, self.x, self.y))
        print(self.x, self.y)
        plt.ioff()
        plt.show()
        # plt.scatter(self.x[:, 0], self.x[:, 1], s=30, color='k')

