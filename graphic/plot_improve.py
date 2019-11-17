import matplotlib.pyplot as plt
import numpy as np
import time
import math

def method_improve(point):
    es_time = np.zeros([point])
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.set_xlabel('Horizontal Position')
    ax.set_ylabel('Vertical Position')
    ax.set_title('Vessel trajectory')

    line = ax.plot([0, 0], [4000, 4000], '-g', marker='*')[0]
    plt.grid(True)  # 添加网格
    plt.ion()  # interactive mode on
    IniObsX = 0000
    IniObsY = 4000
    IniObsAngle = 135
    IniObsSpeed = 10 * math.sqrt(2)  # 米/秒
    print('开始仿真')
    obsX = [0, ]
    obsY = [4000, ]
    for t in range(point):
        t0 = time.time()
        # 障碍物船只轨迹
        obsX.append(IniObsX + IniObsSpeed * math.sin(IniObsAngle / 180 * math.pi) * t)
        obsY.append(IniObsY + IniObsSpeed * math.cos(IniObsAngle / 180 * math.pi) * t)

        line.set_xdata(obsX)
        # line.set_ydata(obsY)
        line.set_data(obsX, obsY)
        ax.set_xlim([-200, 10 * point + 200])
        ax.set_ylim([3800 - 10 * point, 4200])
        # 下面的图,两船的距离
        plt.pause(0.001)
        es_time[t] = 1000 * (time.time() - t0)
    return es_time


def method(point):
    es_time = np.zeros([point])
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.axis("equal")  # 设置图像显示的时候XY轴比例
    ax.set_xlabel('Horizontal Position')
    ax.set_ylabel('Vertical Position')
    ax.set_title('Vessel trajectory')
    plt.grid(True)  # 添加网格
    plt.ion()  # interactive mode on
    IniObsX = 0000
    IniObsY = 4000
    IniObsAngle = 135
    IniObsSpeed = 10 * math.sqrt(2)  # 米/秒
    print('开始仿真')
    for t in range(point):
        t0 = time.time()
        # 障碍物船只轨迹
        obsX = IniObsX + IniObsSpeed * math.sin(IniObsAngle / 180 * math.pi) * t
        obsY = IniObsY + IniObsSpeed * math.cos(IniObsAngle / 180 * math.pi) * t
        ax.scatter(obsX, obsY, c='b', marker='.')  # 散点图
        # 下面的图,两船的距离
        plt.pause(0.001)
        es_time[t] = 1000 * (time.time() - t0)
    return es_time


method(500)
# method_improve(1000)