from typing import Any, Callable




# def lt(a, b):
#     return a < b


def quick_sort(lst):
    compare: Callable[[Any, Any], bool] = lambda a, b: a > b
    return quick_sort(lst, compare)


# def selection_sort(lst, compare):
#     length = len(lst)
#     swp = lst[0]
#
#     pass


class Hole:
    location: int
    value: int

    def __init__(self, location, value):
        self.location = location
        self.value = value


def quick_sort(lst, compare):
    # compare = lt
    # _lst = lst[:]
    length = len(lst)
    if length < 2:
        return lst
    hole = {'loc': 0, 'val': lst[0]}
    swp = lst[0]
    left, right = 0, length
    _round = 1
    while True:
        if left < right:
            if _round % 2 == 1:
                right -= 1
                if compare(lst[right], hole['val']):
                    lst[hole['loc']] = lst[right]
                    hole['loc'] = right
            else:
                left += 1
                if compare(hole['val'], lst[left]):
                    lst[hole['loc']] = lst[left]
                    hole['loc'] = left
            _round += 1
        else:
            lst[hole['loc']] = swp
            break
    if len(lst) > 3:
        lst = quick_sort(lst[0:hole['loc']], compare) \
              + [lst[hole['loc']]] \
              + quick_sort(lst[hole['loc'] + 1:length],
                           compare)
    return lst


def group_by(lst, group_count):
    length = len(lst)
    # groups = []
    # for i in range(0, length, group_count):
    #     groups.append(lst[i:i + group_count])
    # return groups
    groups = [lst[i:i + group_count] for i in range(0, length, group_count)]
    return groups


def merge_sort(lst, compare):
    length = len(lst)
    last = None
    group = []
    if length % 2 == 1:
        last = lst[length - 1]
        lst = lst[0: -1]
    group = group_by(lst, 2)
    group = merge_sort1(group, compare)
    while len(group) > 1:
        True

    return group


def merge_sort1(group, compare):
    return list(map(lambda x: [x[0], x[1]] if compare(x[0], x[1]) else [x[1], x[0]], group))

# def merge(group):






