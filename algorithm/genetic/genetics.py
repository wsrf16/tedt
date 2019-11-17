"""
基因算法
"""
import random
import math
import copy

class Genetic(object):

    @staticmethod
    def replace(string, location, char):
        new = []
        for s in string:
            new.append(s)
        new[location] = char
        return ''.join(new)

    def init_group(self, group_size, length):
        """
        输入：种群大小，染色体长度
        输出：初始化的种群
        """
        group = []
        for i in range(group_size):
            chromeosome = ''
            for j in range(length):
                chromeosome += str(random.randint(0, 1))
            group.append(chromeosome)
        return group

    # xsin(10πx)+2           x ∈ [-1, 2]
    def fitness(self, group, length):
        """
        输入：种群，染色体长度
        输出：种群中各染色体的适应度
        描述：根据排再做染色体的长度，将整段染色体割成两段，然后转换成十进制，带入函数，结果就是适应度
        """
        fitness_list = []
        for i in range(len(group)):
            temp = int(group[i], 2)
            x = -1 + temp * ( 2 - (-1)) / (pow(2, length) -1)
            y = x * math.sin(10 * math.pi * x) + 2
            fitness_list.append(y)
        return fitness_list

    def selection(self, group, length, selection_rate):
        """
        输入：种群，染色体长度
        输出：优胜劣汰的新种群
        描述：选择
        """
        fitness_list = self.fitness(group, length)
        fitness_sum = sum(fitness_list)
        fitness_ratio = 0
        fitness_ratio_list = []
        group_selection = []
        select_count = int(len(group) * selection_rate)

        for fitness in fitness_list:
            fitness_ratio += fitness / fitness_sum
            fitness_ratio_list.append(fitness_ratio)

        for i in range(select_count):
            rand = random.random()

            for j, item in enumerate(group):
                if rand <= fitness_ratio_list[j]:
                    group_selection.append(group[j])
                    break

            # j = 0
            # while j < len(group):
            #     # if rand <= fitness_ratio_list[j]:
            #     #     group_selection.append(group[j])
            #     #     break
            #     # elif fitness_ratio_list[j] < rand <= fitness_ratio_list[j + 1]:
            #     #     group_selection.append(group[j + 1])
            #     #     break
            #     # elif rand >= fitness_ratio_list[j + 1]:
            #     #     j += 1
            #     #     continue
            #
            #     if rand <= fitness_ratio_list[j]:
            #         group_selection.append(group[j])
            #         break
            #     else:
            #         j += 1
            #         continue
        # sorted(group_selection)
        return group_selection

    def crossover(self, group, length, pc):
        """
        输入：种群，交叉率
        输出：优胜劣汰的新种群
        描述：交叉
        """
        crossover = []
        for i in range(len(group)):
            rand_rate = random.random()
            if rand_rate < pc:
                rand_length = random.randint(0, length - 1)
                temp = ''
                if i < len(group) - 1:
                    temp = group[i][:rand_length] + group[i + 1][rand_length:]
                elif i == len(group) - 1:
                    temp = group[i][:rand_length] + group[0][rand_length:]
                crossover.append(temp)
        crossover.extend(group)
        return crossover

    def mutation(self, group, length, pm):
        """
        输入：种群，变异率
        输出：优胜劣汰的新种群
        描述：变异
        """
        mutation = []
        for i in range(len(group)):
            rand_rate = random.random()
            if rand_rate <= pm:
                rand_loc = random.randint(0, length - 1)
                mutant = copy.deepcopy(group[i])
                if mutant[rand_loc] == '0':
                    mutant = Genetic.replace(mutant, rand_loc, '1')
                    # temp[rand_char] = '1'
                elif mutant[rand_loc] == '1':
                    mutant = Genetic.replace(mutant, rand_loc, '0')
                    # temp[rand_char] = '0'
                mutation.append(mutant)
        mutation.extend(group)
        return mutation

    def evolve(self, group, length, selection_rate, crossover_rate, mutation_rate, generations):
        """
        evolution
        :param group: 基因组
        :param length: 基因长度
        :param selection_rate: 选择率
        :param crossover_rate: 交叉率
        :param mutation_rate: 变异率
        :param generations: 进化代数
        :return:
        """
        if generations > 0:
            # fitnesses = self.fitness(samples, 22)
            selections = self.selection(group, length, selection_rate)
            crossovers = self.crossover(selections, length, crossover_rate)
            mutations = self.mutation(crossovers, length, mutation_rate)
            evolution = mutations
            generations -= 1
            return self.evolve(evolution, length, selection_rate, crossover_rate, mutation_rate, generations)
        else:
            return group



    def do(self):
        # 种群大小
        group_size = 500
        # 染色体长度
        length = 22
        selection_rate = 0.5
        crossover_rate = 0.8
        mutation_rate = 0.2
        generations = 20

        group = self.init_group(group_size, length)
        evolution_group = self.evolve(group, length, selection_rate, crossover_rate, mutation_rate, generations)

        results = self.fitness(evolution_group, length)
        result = max(results)
        print("最优解：{0}".format(result))
        return;
