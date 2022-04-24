

def append_to_distinct(ele, lst: list) -> list:
    lst.append(ele)
    d = distinct(lst)
    return d


def distinct(lst: list) -> list:
    d = list(set(lst))
    d.sort(key=lst.index)
    return d

    # visited, queue = set(), [s]
    # while queue:
    #     vertex = queue.pop(0)
    #     if vertex not in visited:
    #         visited.add(vertex)
    #         queue.extend(set(graph[vertex]) - set(visited))
    # return visited





def binary_search(lst: list, num: int):
    low = 0
    high = len(lst)
    loc, val = None, None
    while low < high:
        loc = int((low + high) / 2)
        val = lst[loc]
        if num < val:
            high = loc
        elif num > val:
            low = loc
        else:
            break
    return loc


def fix_sliding_window_most_sum(lst: list, length: int):
    global_sum = 0
    for i, itm in enumerate(lst):
        _sum = sum(lst[i:i + length])
        global_sum = max(global_sum, _sum)
    return global_sum


def sliding_window_n_sum(lst: list, _sum: int):
    results = []
    for i, itm1 in enumerate(lst):
        now = []
        for itm2 in lst[i:len(lst)]:
            now.append(itm2)
            if sum(now) == _sum:
                results.append(now[:])
            elif sum(now) > _sum:
                break
    return results


def brackets1(lst: list):
    length = len(lst)
    left, right = None, None
    new_lst: list = []

    pair = 0
    for i, itm_i in enumerate(lst):
        if itm_i == ')':
            if pair == 0:
                continue
            if pair == 1:
                new_lst.append(itm_i)
                pair = 0
                continue
        elif itm_i == '(':
            if pair == 0:
                new_lst.append(itm_i)
                pair = 1
                left = len(new_lst) - 1
                continue
            if pair == 1:
                continue
        else:
            new_lst.append(itm_i)
    if pair == 1:
        new_lst.pop(left)
    return new_lst










# for j, itm_j in enumerate(lst):
    #     if i > j:
    #         break
    #     if itm_i != ')':
    #         n



