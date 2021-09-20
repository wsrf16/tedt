# class Algorithm


def roulette(fitness_list):
    fitness_sum = sum(fitness_list)
    fitness_p_ratio = 0
    fitness_cumulative_ratio = 0
    fitness_p_ratio_list = []
    fitness_cumulative_ratio_list = []
    for fitness in fitness_list:
        fitness_p_ratio = fitness / fitness_sum
        fitness_cumulative_ratio += fitness_p_ratio
        fitness_p_ratio_list.append(fitness_p_ratio)
        fitness_cumulative_ratio_list.append(fitness_cumulative_ratio)
    return fitness_p_ratio_list, fitness_cumulative_ratio_list
