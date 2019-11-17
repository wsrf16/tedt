from sklearn import preprocessing
from sklearn import linear_model
from sklearn import model_selection
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## 设置字符集，防止中文乱码
mpl.rcParams['font.sans-serif'] = [u'simHei']
mpl.rcParams['axes.unicode_minus'] = False


class SklearnLinearRegression(object):
    """
    # 定义目标函数通过改函数产生对应的y
    # y = 1 * x[0] + 2 * x[1] + .... + (n + 1) * x[n]
    # y = 1 * x[0] + 2 * x[1] + 3 * x[2] + 4 * x[3] + 5 * x[4]
    """
    def ll_model(self, x):
        param_no = np.arange(1, x.shape[-1] + 1)
        y = np.sum(param_no * x, axis=1) + np.random.randn(x.shape[0]) * 0.1
        return y

    def l_model(self, x):
        params_no = np.arange(0, x.shape[0]) + 1
        # params_no = np.arange(1, x.shape[-1] + 1)
        y = np.sum(params_no * x) + np.random.randn(1) * 0.1
        return y

    def get_model(self):
        x = np.random.rand(500, 6)
        param_no = np.arange(0, x.shape[1]) + 1
        y = np.sum(param_no * x, axis=1) + np.random.randn(x.shape[0]) * 0.1
        return x, y

    def action(self):
        # 1.定义数据集
        x = pd.DataFrame(np.random.rand(500, 6))
        y = x.apply(lambda x_rows: pd.Series(self.l_model(x_rows)), axis=1)

        # x, y = self.get_model()

        # 2.划分训练集和测试集
        x_train_processing, x_test_processing, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.3, random_state=2)

        # 3.数据标准化
        # x_train_s = preprocessing.StandardScaler().fit_transform(x_train)
        # 同下
        standardScaler = preprocessing.StandardScaler().fit(x_train_processing)
        x_train = standardScaler.transform(x_train_processing)
        x_test = standardScaler.transform(x_test_processing)

        print(x_train_processing)
        print(x_train)

        # 输出下原数据的标准差和平均数
        print(standardScaler.scale_)
        print(standardScaler.mean_)

        """
        输出为：
        [ 0.29120331  0.28542949  0.27555607  0.29077365  0.29265191  0.27455333]
        [ 0.48993661  0.5081563   0.49650784  0.51339497  0.52648792  0.49551893]
        """

        # 4.训练模型
        linearRegression = linear_model.LinearRegression()
        linearRegression.fit(x_train, y_train)

        print(linearRegression.coef_)
        print(linearRegression.intercept_)

        """
        [[ 0.29420892  0.56808491  0.83138528  1.1669219   1.45715988  1.64179749]]
        [ 10.65847455]
        """

        # 5.用模型预测
        y_test_predict = linearRegression.predict(x_test)
        # linearRegression.score(x_test, y_test)

        ## 预测值和实际值画图比较
        t = np.arange(len(x_test))
        plt.figure(facecolor='w')  # 建一个画布，facecolor是背景色
        plt.plot(t, y_test, 'r-', linewidth=2, label='真实值')
        plt.plot(t, y_test_predict, 'g-', linewidth=1, label='预测值')
        plt.legend(loc='upper left')  # 显示图例，设置图例的位置
        plt.title("线性回归预测真实值之间的关系", fontsize=20)
        plt.grid(b=True)  # 加网格
        plt.show()







