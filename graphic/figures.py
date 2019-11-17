import matplotlib.pyplot as plt


def plot_vertical(x):
    plt.axvline(x=x, ymin=0, ymax=10)


class Figures1(object):
    def do(self):
        plt.subplot(2, 1, 1)
        plot_vertical(20)

        plt.subplot(2, 1, 2)
        plot_vertical(2)

        plt.show()


class Figures2(object):
    def do(self):
        plt.figure(1)
        plot_vertical(1)
        plt.figure(2)
        plot_vertical(2)

        plt.show()

