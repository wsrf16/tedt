from typing import List


def mid_find(lst, key, target: int) -> List[int]:
    new_lst = wrap_find(lst, key)
    ret = mid_find1(new_lst, target)
    return ret


def mid_find1(lst, target):
    length = len(lst)
    mid = int(length / 2)
    if target < lst[0]['val'] or target > lst[length-1]['val']:
        return None

    if target < lst[mid]['val']:
        return mid_find1(lst[0: mid], target)
    elif target > lst[mid]['val']:
        return mid_find1(lst[mid + 1:], target)
    elif target == lst[mid]['val']:
        return lst[mid]['loc'], lst[mid]['val']
    else:
        return None


def wrap_find(lst, key):
    new_lst = []
    for loc, val in enumerate(lst):
        cur = {'loc': loc, 'val': key(val)}
        new_lst.append(cur)

    new_lst = sorted(new_lst, key=lambda c: c['val'])
    return new_lst
