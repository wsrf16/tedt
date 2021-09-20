from collections import Sequence
from typing import List
from collections import deque


class Next(object):
    def __init__(self, oper, num):
        self.operation = oper
        self.num = num
        self.passed = []

    def compute(self, source):
        result = 0
        if self.oper == '+':
            result = source + self.num
        elif self.oper == '-':
            result = source - self.num
        elif self.oper == '*':
            result = source * self.num
        elif self.oper == '/':
            result = source / self.num
        return result

    # def append(self, next):
    #     self.passed.append(next)
    #     return


class FirstSearch1(object):
    # def __init__(self, a)

    def bfs(self):
        next1 = Next('*', 2)
        next2 = Next('+', 5)
        next3 = Next('-', 3)
        next_list = [next1, next2, next3]
        optimum = 4
        passed = []
        self.compute(4, passed, next_list)
        return

    def compute(self, source, passed: List[Next], next_list: List[Next]):
        # passed.append(Next('*', 2))
        for next in next_list:
            new_source = next.compute(source)


class FirstSearch2(object):
    def __init__(self):
        self.graph = {
            'A': ['B', 'C'],
            'B': ['A', 'C', 'D'],
            'C': ['A', 'B', 'D', 'E'],
            'D': ['B', 'C', 'E', 'F'],
            'E': ['C', 'D'],
            'F': ['D']
        }
        # self.graph = {
        #     '台湾': ['福建'],
        #     '海南': ['广东'],
        #     "内蒙古": ["黑龙江", "吉林", "辽宁", "河北", "山西", "陕西", "宁夏", "甘肃"],
        #     "黑龙江": ["内蒙古", "吉林"],
        #     "吉林": ["黑龙江", "内蒙古", "辽宁"],
        #     "辽宁": ["吉林", "内蒙古", "河北"],
        #     "河北": ["辽宁", "内蒙古", "山西", "北京", "天津", "山东", "河南"],
        #     '河南': ['河北', '湖北', '陕西', '山西', '安徽', '山东'],
        #     "山东": ["河北", "河南", '安徽', '江苏'],
        #     "北京": ["河北", "天津"],
        #     "天津": ["河北", "北京"],
        #     "山西": ["河北", "内蒙古", "陕西", "河南"],
        #     "陕西": ["宁夏", "内蒙古", "甘肃", "河南", "山西", "四川", "重庆", "湖北"],
        #     "宁夏": ["陕西", "内蒙古", "甘肃"],
        #     "甘肃": ["宁夏", "内蒙古", "陕西", "青海", "新疆", "四川"],
        #     "青海": ["甘肃", "西藏", "新疆", "四川"],
        #     "新疆": ["西藏", "甘肃", "青海"],
        #     "西藏": ["新疆", "青海", "四川", "云南"],
        #     "四川": ["青海", "西藏", "甘肃", "陕西", "云南", "贵州", "重庆"],
        #     '云南': ['西藏', '四川', '贵州', '广西'],
        #     '重庆': ['陕西', '四川', '贵州', '湖南', '湖北'],
        #     '贵州': ['重庆', '四川', '云南', '广西', '湖南'],
        #     '广西': ['云南', '贵州', '湖南', '广东'],
        #     '广东': ['福建', '江西', '湖南', '广西', '香港', '澳门', '海南'],
        #     '湖南': ['湖北', '重庆', '贵州', '广西', '广东', '江西'],
        #     '江西': ['安徽', '湖北', '湖南', '广东', '福建', '浙江'],
        #     '福建': ['浙江', '江西', '广东', '台湾'],
        #     '湖北': ['河南', '陕西', '重庆', '湖南', '江西', '安徽'],
        #     '河南': ['河北', '山西', '陕西', '湖北', '安徽', '江苏', '山东'],
        #     '安徽': ['河南', '湖北', '江西', '浙江', '江苏', '山东'],
        #     '浙江': ['上海', '江苏', '安徽', '江西', '福建'],
        #     '上海': ['江苏', '浙江'],
        #     '江苏': ['山东', '安徽', '浙江', '上海'],
        #     '山东': ['河北', '河南', '江苏'],
        #     '香港': ['广东'],
        #     '澳门': ['广东'],
        # }


    ####################################
    def do(self):
        parent, path = dfs(self.graph, 'D')
        self.parse(parent)
        return

    def parse(self, bfs):
        for k in bfs:
            route = "出发->"
            while k is not None:
                route += k + "->"
                k = bfs[k]
            route += "到啦！"
            print(route)


def bfs(graph, s):
    return _do(graph, s, 'bfs')


def dfs(graph, s):
    return _do1(graph, s, 'dfs')


def _do1(graph, s, bfs_or_dfs: str = 'bfs'):
    # visited：全局已经走过的节点
    # to_visit：本轮待走节点（未走过的节点），用于下一轮走
    visited, to_visit = set([s]), [s]
    parent = {s: None}
    path = []
    while len(to_visit) > 0:
        # 取
        current = to_visit.pop(0) if bfs_or_dfs == 'bfs' else to_visit.pop()
        nexts = graph[current]
        # nexts = list(set(graph[current]) - set(visited))
        path.append(current)
        for next in nexts:
            # 放
            if next not in visited:
                to_visit.append(next)
                visited.add(next)
                parent[next] = current
    return parent, path


def _do(graph, s, bfs_or_dfs: str = 'dfs'):
    # visited：全局已经走过的节点
    # to_visit：本轮待走节点（未走过的节点），用于下一轮走
    visited, to_visit = [], [s]
    parent = {s: None}
    while to_visit:
        # 取
        current = to_visit.pop(0) if bfs_or_dfs == 'bfs' else to_visit.pop()
        # visited = append_to_distinct(current, visited)
        if current not in visited:
            visited.append(current)
        for next in graph[current]:
            # 放
            if next not in visited:
                to_visit.append(next)
                parent[next] = current
    return parent, visited











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











