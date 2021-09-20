import copy


def enumerate_list(moneys):
    total_solution = []

    def inner(total, solution):
        for item in moneys:
            if total == item:
                solution.append(item)
                total_solution.append(solution)
            if total > item:
                new_solution = copy.deepcopy(solution)
                new_solution.append(item)
                inner(total - item, new_solution)
        return total_solution

    return inner
