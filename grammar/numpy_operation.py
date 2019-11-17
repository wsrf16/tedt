import numpy as np
import os


class Operation(object):

    def do(self):
        x = np.array([[1, 2], [3, 4]])

        n = 2
        y1 = x + n
        y2 = x * n

        n = np.array([[5, 7]])
        y1 = x + n
        y2 = x * n

        n = np.array([[5], [7]])
        y1 = x + n
        y2 = x * n

        n = np.array([[5, 7], [11, 13]])
        y1 = x + n
        y2 = x * n

        os.system("pause");
