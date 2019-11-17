import json
# import yaml
from ruamel import yaml


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, int):
            return int(obj)
        elif isinstance(obj, float):
            return float(obj)
        elif isinstance(obj, list):
            return obj.tolist()
        elif isinstance(obj, str):
            return obj.__str__()
        elif isinstance(obj, dict):
            return dict(obj)
        else:
            return super(MyEncoder, self).default(obj)


def json_serialize(obj):
    # obj_dic = class2dic(obj)
    obj_dic = value2py_data(obj)

    return yaml.safe_dump(obj_dic)


def class2dic(obj):
    obj_dic = obj.__dict__

    for key in obj_dic.keys():
        value = obj_dic[key]
        obj_dic[key] = value2py_data(value)

    return obj_dic


def value2py_data(value):
    #__main__
    if str(type(value)).__contains__('.'):
        # value 为自定义类
        value = class2dic(value)

    elif str(type(value)) == "<class 'list'>":
        # value 为列表
        for index in range(0, value.__len__()):
            value[index] = value2py_data(value[index])

    return value


class Parent(object):
    def __init__(self, son, a, b):
        self.son = son
        self.a = a
        self.b = b


class Son(object):
    def __init__(self, c, d):
        self.c = c
        self.d = d


def do():
    son1 = Son(['c1', 'c2'], 'd')
    son2 = Son(['c1', 'c2'], 'd')
    parent = Parent([son1, son2], 'a', 'b')
    # jjj = json.dumps(parent)
    # print(jjj)
    text = json_serialize(parent)
    aaa= json.dumps(parent, cls=MyEncoder)

    print(text)


    # if isinstance(text, Son):
    #     return int(text)