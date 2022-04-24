import numpy as np


# BucketSort
def BucketSort(a, n):
    barrel = {}
    for i in range(0, n):
        barrel.setdefault(i, [])
    min = np.min(a)
    max = np.max(a)
    for x in a:
        for i in range(0, n - 1):
            if min + i * (max - min) / n <= x < min + (i + 1) * (max - min) / n:
                barrel[i].append(x)
            elif i == n - 2 and x >= min + (i + 1) * (max - min) / n:
                barrel[i+1].append(x)
    k = 0
