
FAKE_PREFIX = '_'


def __model2dict(model):
    obj_dic = model.__dict__
    modify_list = []

    for key in obj_dic.keys():
        # new_key = str(key).strip('_') if str(key).__contains__(FAKE_PREFIX) else key
        if not (modify_list.__contains__(key)):
            # value = obj_dic[key]
            # obj_dic[key] = any2dict(value)
            if str(key).__contains__(FAKE_PREFIX):
                new_key = str(key).strip(FAKE_PREFIX)
                value = obj_dic[key]
                obj_dic[new_key] = value
                obj_dic.pop(key)
                modify_list.append(new_key)
            else:
                value = obj_dic[key]
                obj_dic[key] = obj2dict(value)
    return obj_dic


def obj2dict(value):
    if str(type(value)).__contains__('.'):
        value = __model2dict(value)
    elif str(type(value)) == "<class 'list'>":
        # value 为列表
        for index in range(0, value.__len__()):
            value[index] = obj2dict(value[index])
    return value


class ClassIterator:
    def __init__(self):
        self.iter_keys = []

    # 对象转字典必须实现的方法,自动调用获取需要dict化的属性名
    def keys(self):
        return self.iter_keys

    # 对象模式序列化成dict必须实现的方法,和keys方法配合返回dict属性的value
    def __getitem__(self, key):
        return getattr(self, key)

    # 可以动态隐藏不需要返回的属性名
    def hide(self, *keys):
        for key in keys:
            self.iter_keys.remove(key)
        # 兼容链式调用(非常适合列表推导式)
        return self

    # 可以动态增加需要返回的属性名
    def append(self, *keys):
        for key in keys:
            self.iter_keys.append(key)
        # 兼容链式调用(非常适合列表推导式)
        return self
