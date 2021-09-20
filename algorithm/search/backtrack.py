class Backtrack1(object):
    # def __init__(self):
    #     self.result = []

    def todo(self):
        result = self.do(['a', 'e', 'i', 'o', 'u'])
        return result

    def do(self, source: list) -> list:

        buffer, result_list = [], []
        self._fill(source, buffer, result_list)
        return result_list

    def _fill(self, source: list, buffer, result_list):
        # 到达叶子节点，将路径装入结果列表
        if len(buffer) == len(source):
            result_list.append(buffer[:])
            return

        for i in source:
            if i not in buffer:
                buffer.append(i)
                self._fill(source, buffer, result_list)
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
        self._fill(source, target_sum, buffer, result_list)
        return result_list

    def _fill(self, source: list, target_sum, buffer, result_list):
        if len(buffer) == 3:
            if sum(buffer) == target_sum:
                result_list.append(buffer[:])
            return
        for i in source:
            if i not in buffer:
                buffer.append(i)
                self._fill(source, target_sum, buffer, result_list)
                buffer.pop()

