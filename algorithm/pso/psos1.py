import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import enum


class PSO(object):
    def __init__(self, population_size, max_gen_steps):
        self.w = 0.6                                                    # 惯性权重
        self.c1 = self.c2 = 2                                           # 随机数
        self.population_size = population_size                          # 粒子群数量
        self.max_gen_steps = max_gen_steps                              # 进化迭代次数
        self.DIM = 2                                                    # 搜索空间的维度
        self.X_BOUND = [-10, 10]                                        # 解空间范围
        self.x = np.random.uniform(self.X_BOUND[0], self.X_BOUND[1],
                                   (self.population_size, self.DIM))    # 初始化粒子群位置
        self.v = np.random.rand(self.population_size, self.DIM)         # 初始化粒子群速度
        fitness = self.calculate_fitness(self.x)
        self.p_best = self.x                                            # 个体的最佳位置
        self.g_best = self.x[np.argmin(fitness)]                        # 全局最佳位置
        self.individual_best_fitness = fitness                          # 个体的最优适应度
        self.global_best_fitness = np.max(fitness)                      # 全局最佳适应度

    def calculate_fitness(self, x):
        return np.sum(np.square(x), axis=1)

    def evolve(self):
        for step in range(self.max_gen_steps):
            r1 = np.random.rand(self.population_size, self.DIM)
            r2 = np.random.rand(self.population_size, self.DIM)
            # 更新速度和权重
            self.v = self.w * self.v + self.c1 * r1 * (self.p_best - self.x) + self.c2 * r2 * (self.g_best - self.x)
            self.x = self.v + self.x
            plt.clf()
            plt.scatter(self.x[:, 0], self.x[:, 1], s=30, color='k')
            plt.xlim(self.X_BOUND[0], self.X_BOUND[1])
            plt.ylim(self.X_BOUND[0], self.X_BOUND[1])
            plt.pause(0.01)
            fitness = self.calculate_fitness(self.x)
            # 需要更新的个体
            # false true false true
            update_id = np.greater(self.individual_best_fitness, fitness)
            self.p_best[update_id] = self.x[update_id]
            self.individual_best_fitness[update_id] = fitness[update_id]
            # 新一代出现了更小的fitness，所以更新全局最优fitness和位置
            if np.min(fitness) < self.global_best_fitness:
                self.g_best = self.x[np.argmin(fitness)]
                self.global_best_fitness = np.min(fitness)
            print('best fitness: %.5f, mean fitness: %.5f' % (self.global_best_fitness, np.mean(fitness)))
    plt.show()
