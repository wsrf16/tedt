import numpy
import pandas
import csv
import os
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')



# 核心代码，设置显示的最大列、宽等参数，消掉打印不完全中间的省略号
pandas.set_option('display.max_columns', 1000)
pandas.set_option('display.width', 1000)
pandas.set_option('display.max_colwidth', 1000)
numpy.set_printoptions(threshold=1000)

# %matplotlib inline


# data = {'city': {0: 'beijing', 1: 'shanghai', 2: 'guangzhou', 3: 'shenzhen'},
#         'pop': {0: 1.1, 1: 1.2, 2: 1.3, 3: 1.4},
#         'year': {0: 2018, 1: 2017, 2: 2018, 3: 2016}
#         }
# frame = pandas.DataFrame(data)
# print(frame)
#
# dd = numpy.array([1, 2, 3.3, 'kk'])
# print(dd.dtype)
#
# zimu = ['a', 'b', 'c', 'd', 'e', 'f']
# print('a' in zimu)
#
# (month, day) = (4, 15)
# days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (12, 23))
# days = filter(lambda x: x <= (month, day), days)
# print(list(days))
#
# exit()

def print_last(a):
    print(a);
    exit(0)

dir_csv = ".\\algorithm\\recommendation\\";
class Statistics:
    def do(self):

        print(os.getcwd())
        # aaa=csv.reader(open('ratings.csv'), 'r')

        rate = pandas.read_csv(dir_csv + 'ratings.csv', sep=',', header=0)
        # rate = pandas.read_csv('ratings.csv', sep=',', header=0, names=['user_id', 'movie_id', 'rating', 'titmestamp'])
        # print_last(rate)
        movie = pandas.read_csv(dir_csv + 'movies.csv')
        # print_last(movie)

        df = pandas.merge(rate, movie, on='movieId')
        # <class 'pandas.core.series.Series'>

        ratings = pandas.DataFrame(df.groupby('title')['rating'].mean(), columns=['rating']) #.sort_values(by='rating', ascending=False)
        # print_last(ratings)
        ratings['number_of_ratings'] = df.groupby('title')['rating'].count() #.sort_values(ascending=False)
        # print_last(ratings)

        # 透视表
        movie_matrix = df.pivot_table(index='userId', columns='title', values='rating')
        # movie_matrix = movie_matrix.fillna(0) #.sort_values()
        # print_last(movie_matrix)

        # 相似度
        air_force_one_user_rating = movie_matrix['Air Force One (1997)']#.sort_values(ascending=False)
        contact_user_rating = movie_matrix['Contact (1997)']#.sort_values(ascending=False)
        til_user_rating = movie_matrix['\'Til There Was You (1997)']#.sort_values(ascending=False)
        # print_last(air_force_one_user_rating)

        # 计算相似度
        similar_to_air_force_one = movie_matrix.corrwith(air_force_one_user_rating)#.sort_values(ascending=False)
        similar_to_contact = movie_matrix.corrwith(contact_user_rating)  # .sort_values(ascending=False)
        similar_to_til = movie_matrix.corrwith(til_user_rating)#.sort_values(ascending=False)
        # pandas.DataFrame()

        # print_last(similar_to_air_force_one['\'Til There Was You (1997)'])
        # print_last(similar_to_air_force_one['Air Force One (1997)'])
        print_last(similar_to_air_force_one)
        print_last(similar_to_til)

        # 直方图
        plt.figure(figsize=(8, 6))
        plt.rcParams['patch.force_edgecolor'] = True

        ratings['rating'].hist(bins=50)
        ratings['number_of_ratings'].hist(bins=60)

        # 散点图
        sns.set_style('dark')
        sns.jointplot(x='rating', y='number_of_ratings', data=ratings)

        plt.show()


        # print(movie)




