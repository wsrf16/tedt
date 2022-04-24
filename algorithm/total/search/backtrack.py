import codecs
import itertools
import random
from typing import List

import numpy as np


class Backtrack1(object):
    # def __init__(self):
    #     self.result = []

    def do(self, source: List[int]) -> List[int]:
        buffer, result_list = [], []
        self.fill(source, buffer, result_list)
        return result_list

    def backtrack(self, source: List[int], buffer, result_list):
        # 到达叶子节点，将路径装入结果列表
        if len(buffer) == len(source):
            result_list.append(buffer[:])
            return

        for i in source:
            if i not in buffer:
                buffer.append(i)

                # if len(buffer) == len(source):
                #     result_list.append(buffer[:])
                #     break
                self.backtrack(source, buffer, result_list)
                buffer.pop()


class Backtrack2(object):
    def todo(self):
        result = self.do(1, 15, 15)
        return result

    def do(self, frm, to, target_sum):
        source = []
        for i in range(frm, to):
            source.append(i)
        buffer, result_list = [], []
        self.backtrack(source, target_sum, buffer, result_list)
        return result_list

    def backtrack(self, source: list, target_sum, buffer, result_list):
        if len(buffer) == 3:
            if sum(buffer) == target_sum:
                result_list.append(buffer[:])
            return
        for i in source:
            if i not in buffer:
                buffer.append(i)
                self.backtrack(source, target_sum, buffer, result_list)
                buffer.pop()














def queen(num: int):
    board = np.zeros([num, num], dtype=int)
    stack = []
    result = [np.zeros([num, num], dtype=int)]
    place(board, stack, result)
    return


def check_8_queen(grid, row, col):
    dim = len(grid[0])

    if (1 in grid[row] or 1 in grid[:, col]) and grid[row][col] != 1:
        return False

    i = row
    j = col
    while 0 <= i < dim and 0 <= j < dim:
        if i != row and j != col and 1 == grid[i][j]:
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while 0 <= i < dim and 0 <= j < dim:
        if i != row and j != col and 1 == grid[i][j]:
            return False
        i += 1
        j += 1

    i = row
    j = col
    while 0 <= i < dim and 0 <= j < dim:
        if i != row and j != col and 1 == grid[i][j]:
            return False
        i += 1
        j -= 1

    i = row
    j = col
    while 0 <= i < dim and 0 <= j < dim:
        if i != row and j != col and 1 == grid[i][j]:
            return False
        i -= 1
        j += 1

    return True


def place(source, stack: List[int], result: List[np.ndarray]):
    dim = len(source[0])

    row = len(stack) if len(stack) > 0 else 0
    if row > dim - 1:
        result[0] = source.copy()
        return True

    for i in range(dim):
        if check_8_queen(source, row, i):
            stack.append(i)
            source[row][i] = 1
            if place(source, stack, result):
                return True
            # place(source, stack)
            stack.pop()
            source[row][i] = 0

    return False










def sudoku():
    file = open("quiz.txt", "r", encoding='UTF-8')
    row = file.read().encode('utf-8').decode('utf-8-sig').split('\n')
    grid = []
    grid
    for line in row:
        grid.append(list(line.strip().split(' ')))
    grid = np.array(grid, dtype=int)
    stack = []
    result = [np.array([])]
    fill(grid, stack, result)
    aaaa = np.array(['a', 'b', 'c', 'a'])
    return


def fill(source: np.ndarray, stack: List[int], result: List[np.ndarray]):
    if all(x in range(1, 10) for x in itertools.chain(*source)):
    # if np.array([x in range(1, 10) for x in itertools.chain(*source)]).all():
        result[0] = source.copy()
        return True

    for i in range(9):
        for j in range(9):
            if source[i, j] not in range(1, 10):
                for itm in range(1, 10):
                    if check_sudoku(source, i, j, itm):
                        stack.append([i, j, itm])
                        empty = source[i, j]
                        source[i, j] = itm
                        fill(source, stack, result)
                        # if fill(source, stack):
                        #     return True
                        stack.pop()
                        source[i, j] = empty
                return False
    return False


def check_sudoku(grid: List[int], i, j, val):
    # row, column
    if (val in grid[i] or val in grid[:, j]) and grid[i][j] != val:
        return False

    # 9 square
    zone_x, zone_y = [], []
    for itm in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
        if i in itm:
            zone_x = itm
    for itm in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
        if j in itm:
            zone_y = itm

    if not all([grid[x][y] != val for x in zone_x for y in zone_y]):
        return False

    # for x in zone_x:
    #     for y in zone_y:
    #         if val == grid[x][y]:
    #             return False
    return True


