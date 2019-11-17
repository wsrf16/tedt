import json
from common import dictionary


def any2json(obj):
    dict = dictionary.obj2dict(obj)
    return json.dumps(dict)


def file2dict(file):
    with open(file, 'r', encoding='utf-8') as stream:
        dict = json.load(stream)
        return dict


def dict2file(dict, file):
    with open(file, 'w', encoding='utf-8') as stream:
        json.dump(dict, stream)

