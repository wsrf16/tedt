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

    def knapsack(self):
        articles = [
            {'no': 0, 'v': 6, 'w': 3},
            {'no': 1, 'v': 10, 'w': 1},
            {'no': 2, 'v': 5, 'w': 2},
            {'no': 3, 'v': 10, 'w': 4},
        ]
        capacity = 6
        graph: np.ndarray = np.zeros([len(articles), capacity + 1])
        for i in range(graph.shape[0]):
            for j in range(graph.shape[1]):
                row = graph[i]
                if i == 0:
                    if articles[i].get('w') <= j:
                        row[j] = articles[i].get('v')
                    else:
                        row[j] = 0
                else:
                    if articles[i].get('w') <= j:
                        do_take = articles[i].get('v') + graph[i - 1][j - articles[i].get('w')]
                        not_take = graph[i - 1][j]
                        row[j] = max(do_take, not_take)
                    else:
                        row[j] = graph[i - 1][j]
        return graph



    def do_nearest(self):
        grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
        self.nearest(grid)

    def nearest(self, grid: list):
        dp = np.zeros([len(grid), len(grid[0])])
        # path = []
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j]+dp[i][j-1]
                elif j == 0:
                    dp[i][j] = grid[i][j]+dp[i-1][j]
                else:
                    dp[i][j] = min(grid[i][j]+dp[i][j-1], grid[i][j]+dp[i-1][j])
                    # if grid[i][j]+dp[i][j-1] <= grid[i][j]+dp[i-1][j]:
                    #     path.append([i, j-1])
                    # elif grid[i][j]+dp[i][j-1] >= grid[i][j]+dp[i-1][j]:
                    #     path.append([i-1, j])
        return dp

