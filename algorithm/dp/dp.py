import numpy as np


class DP(object):
    # 递归
    def cmp1(self, no):
        if no == 1:
            result = 1
        elif no == 2:
            result = 2
        else:
            result = self.cmp1(no - 1) + self.cmp1(no - 2)
        return result

    # 循环
    def cmp2(self, no):
        if no == 1:
            return 1
        elif no == 2:
            return 2
        else:
            a = self.cmp2(1)
            b = self.cmp2(2)
            for i in range(3, no + 1):
                a, b = b, a + b
            return a + b

    def bag(self):
        graph: np.ndarray = np.zeros([4, 7])
        articles = [
            {'no': 0, 'v': 6, 'w': 3},
            {'no': 1, 'v': 10, 'w': 1},
            {'no': 2, 'v': 5, 'w': 2},
            {'no': 3, 'v': 10, 'w': 4},
        ]
        for i in range(graph.shape[0]):
            for j in range(graph.shape[1]):
                row = graph[i]
                if i == 0:
                    if j < articles[i].get('w'):
                        row[j] = 0
                    else:
                        row[j] = articles[i].get('v')
                else:
                    if j < articles[i].get('w'):
                        row[j] = graph[i - 1][j]
                    else:
                        do_take = articles[i].get('v') + graph[i - 1][j - articles[i].get('w')]
                        not_take = graph[i - 1][j]
                        row[j] = max(do_take, not_take)
        return graph
