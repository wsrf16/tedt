import pandas
import numpy
import matplotlib.pyplot as plt

class MatplotlibPyplot():
    def do(self):
        print(numpy.random.randn(6,4))

        index = pandas.date_range('20170220',periods=6)
        print(index)
        data = pandas.DataFrame(numpy.random.randn(6,4),index=index,columns=list('ABCD'))
        print(data)

        d_data = {'A':1,'B':pandas.Timestamp('20170220'),'C':range(4),'D':numpy.arange(4)}
        print(d_data)
        df_data = pandas.DataFrame(d_data)
        print(df_data)


        x1 = [30.89, 17.24, 13.82, 13.00, 12.47]  # Make x, y arrays for each graph
        y1 = [47.769, 46.055, 44.176, 41.844, 39.476]
        x2 = [29.21, 16.76, 13.70, 13.02, 12.21]
        y2 = [47.761, 46.02, 44.096, 41.744, 39.359]

        plt.plot(x1, y1, 'r', label='original')
        plt.legend()
        plt.show()

