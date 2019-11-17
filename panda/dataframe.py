import pandas
import numpy

pandas.set_option('display.max_columns', 1000)
pandas.set_option('display.width', 1000)
pandas.set_option('display.max_colwidth', 1000)


data = {'city': {0: 'beijing', 1: 'shanghai', 2: 'guangzhou', 3: 'shenzhen'},
        'pop': {0: 1.1, 1: 1.2, 2: 1.3, 3: 1.4},
        'year': {0: 2018, 1: 2017, 2: 2018, 3: 2016}
        }
df = pandas.DataFrame(data, columns= ['year', 'city', 'pop'])
print(df)
exit(0)


indexes = pandas.date_range('20170220', periods=6)
indexes = indexes.append(indexes)
print(indexes)

datas = numpy.random.randn(12, 4)
print(datas)

frame = pandas.DataFrame(data = datas, index = indexes, columns = list('ABCD'))
frame['E']=indexes
print(frame)

_groupby = frame.groupby('E')['A'].sum()
print(_groupby)