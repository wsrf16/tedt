# import yaml
from common import dictionary
import ruamel.yaml
from playhouse.shortcuts import model_to_dict,dict_to_model


def obj2yaml(obj):
    _dict = dictionary.obj2dict(obj)
    _bytes = ruamel.yaml.safe_dump(_dict, default_flow_style=False, encoding='utf-8', allow_unicode=True)
    return str(_bytes, encoding="utf-8")


def dict2yaml(_dict):
    _bytes = ruamel.yaml.safe_dump(_dict, default_flow_style=False, encoding='utf-8', allow_unicode=True)
    return str(_bytes, encoding="utf-8")


def yaml2dict(yaml):
    # dict = dictionary.any2dict(obj)
    _dict = ruamel.yaml.safe_load(yaml, None)
    return _dict


def file2dict(file):
    with open(file, 'r', encoding='utf-8') as stream:
        _dict = ruamel.yaml.load(stream, Loader=ruamel.yaml.Loader)
        return _dict


# def dict2file(dict, file):
#     with open(file, 'w', encoding='utf-8') as stream:
#         yaml.safe_dump(dict, stream=stream, default_flow_style=False)

def dict2file(_dict, file):
    with open(file, 'w', encoding='utf-8') as stream:
        ruamel.yaml.safe_dump(_dict, stream=stream, default_flow_style=False)
