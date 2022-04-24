class Bayes:
    """
    假设有两个各装了100个球的箱子，甲箱子中有70个红球，30个绿球，乙箱子中有30个红球，70个绿球。
    假设随机选择其中一个箱子，从中拿出一个球记下球色再放回原箱子，如此重复12次，记录得到8次红球，
    4次绿球。问题来了，你认为被选择的箱子是甲箱子的概率有多大？
    """

    @staticmethod
    def bayes_function(p_red_a, p_a, p_red_b, p_b):
        ret = (p_red_a * p_a) / ((p_red_a * p_a) + (p_red_b * p_b))
        return ret

    def red(self, times):
        p_red_a = 0.7
        p_a = 0.5
        p_red_b = 0.3
        p_b = 1 - p_a
        for i in range(times):
            p_a = Bayes.bayes_function(p_red_a, p_a, p_red_b, p_b)
            p_b = 1 - p_a
            print("%s times p_a:  %s" % (i + 1, p_a))

    def do(self):
        times = 8
        self.red(times)
