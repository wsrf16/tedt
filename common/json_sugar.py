import json
from common import dictionary


def any2json(obj):
    # dict = obj.__dict__
    dict = dictionary.obj2dict(obj)
    return json.dumps(dict)

# def convert2json(dict_json):
#   return Person(dict_json['name'], dict_json['age'], dict_json['email'])
#
# def json2any(json):
#     return json.loads(json, object_hook: convert2json)


def file2dict(file):
    with open(file, 'r', encoding='utf-8') as stream:
        dict = json.load(stream)
        return dict


def dict2file(dict, file):
    with open(file, 'w', encoding='utf-8') as stream:
        json.dump(dict, stream)

