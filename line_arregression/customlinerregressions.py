# # import
#
#
# # 根据y=2*x+b随意写几个数
# X = [1, 2, 3, 4, 5, 6, 7]
# Y = [3.09, 5.06, 7.03, 9.12, 10.96, 12.91, 15.01]
# Xsum = 0.0
# X2sum = 0.0
# Ysum = 0.0
# XY = 0.0
# n = len(X)
# for i in range(n):
#     Xsum += X[i]
#     Ysum += Y[i]
#     XY += X[i] * Y[i]
#     X2sum += X[i] ** 2
# k = (Xsum * Ysum / n - XY) / (Xsum ** 2 / n - X2sum)
# b = (Ysum - k * Xsum) / n
# print('the line is y=%f*x+%f' % (k, b))
