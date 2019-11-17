# -*-coding: UTF-8 -*-

# python2
# sys.setdefaultencoding('utf-8')

import sys

print(sys.path)
import algorithm.bayes.bayes as bayes
import numpy as np
from algorithm.recommendation import recommendation
from algorithm.genetic import genetics
from algorithm.pso import psos1
from algorithm.pso import psos2
from algorithm.simulate_dannealing import sa

from graphic import figures
import matplotlib.pyplot as plt

# 不显示
# plt.switch_backend('Agg')
# 显示
plt.switch_backend('TkAgg')

from line_arregression import sklearns
from feature import qdingloginsample
from grammar import classdemo
from grammar import json_sample
from grammar import argumentsdemo
from grammar import numpy_operation

import common.yaml_sugar
from common import Bean
from common import dictionary


class C(object):
    def __init__(self):
        self.abc = 'abc'


class Foo(object):
    def __init__(self):
        self.a = 1
        self.b = '1'
        self.c = C()


foo = Foo()
d = {"a": "b", "c": {"d": "e"}}
obj = Bean.Dict2Obj(d)
print(obj.a)
print(obj.c)
print(obj.c.d)

dic = dictionary.obj2dict(foo)

aa = {'a': '赵煜'}
yml = common.yaml_sugar.obj2yaml(foo)
obj = common.yaml_sugar.yaml2dict(yml)
yml = common.yaml_sugar.obj2yaml({'a': '赵煜'})

# matplotlib的默认backend是TkAgg，而FltkAgg, GTK, GTKAgg, GTKCairo, TkAgg , Wx or WxAgg这几个backend都要求有GUI图形界面的。
# 会提示：Backend TkAgg is interactive backend. Turning interactive mode on.
# 方案：改为指定不需要GUI的backend（Agg, Cairo, PS, PDF or SVG）


# a = np.arange(10).reshape(2,-1)
# b = np.repeat(1, 10).reshape(2,-1)
#
# # Answers
# # Method 1:
# c = np.concatenate([a, b], axis=0)
#
# # Method 2:
# d = np.vstack([a, b])


# x = np.array([[1, 2], [3, 4]])
# n = np.array([[5, 7]])
# n = np.array([[5, 7, 1]])
# n = np.array([[5, 7]])
#
#
#
#
# A = np.array([[2],[1],[3]])
# b = np.transpose(np.array([[2, 1, 3]]))
# c = np.array([[2, 1, 3]]).T
# b = np.transpose(np.array([[-3, 5, -2]]))


datas = np.arange(5)
datas = datas[datas % 2 == 0]

x = np.array([[1, 2], [3, 4]])
n = np.array([[5], [7]])

y = x + n

# lst = [1,2,3,4,5,6,7,8,9]
# aa = lst[lst % 2 == 0]
#
# exit(0)

operate = 'bayes'
operate = 'recommendation'
operate = 'pppppp'
operate = 'figures'
operate = 'numpyoperation'
operate = 'sklearn_linear_regression'
operate = 'arguments'
operate = 'imported'
operate = 'classdemo'
operate = 'ldap'
operate = 'jsonsample'
operate = 'sa'
operate = 'genetic'
operate = 'pso2'
operate = 'pso1'

if operate == 'recommendation':
    recommendation_instance = recommendation.Statistics()
    recommendation_instance.do()
elif operate == 'genetic':
    genetic_instance = genetics.Genetic()
    genetic_instance.do()
elif operate == 'bayes':
    baye = bayes.Bayes()
    baye.do()
elif operate == 'pso1':
    pso = psos1.PSO(100, 100)
    pso.evolve()
elif operate == 'pso2':
    pso = psos2.PSO2(50, 200, psos2.ExtremeEnum.MIN)
    pso.evolve()
elif operate == 'arguments':
    arg = argumentsdemo.ArgumentsDemo()
    arg.do()
elif operate == 'sa':
    sa = sa.SA()
    sa.evolve()
elif operate == 'figures':
    # figures1 = figures.Figures1()
    # figures1.do()
    figures2 = figures.Figures2()
    figures2.do()
elif operate == 'sklearn_linear_regression':
    sklearn_linear_regression = sklearns.SklearnLinearRegression()
    sklearn_linear_regression.action()
elif operate == 'numpyoperation':
    operation = numpy_operation.Operation()
    operation.do()
elif operate == 'imported':
    import importlib

    module = __import__('practise.show')
    module.show.showme()
    module.show.showme()

    module_t = importlib.import_module('practise.show')
    module_t.showme()
elif operate == 'ldap':
    qdingloginsample.do()
elif operate == 'classdemo':
    classdemo.Car('name')
elif operate == 'jsonsample':
    json_sample.do()
elif operate != 'pppppp':
    exit(0)
