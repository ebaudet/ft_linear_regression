#!/usr/bin/env python3
# coding: utf-8
import csv
import matplotlib.pyplot as plt
import numpy as np
import fire

C_RED = '\033[91m'
C_GREEN = '\033[92m'
C_YELLOW = '\033[93m'
C_LIGHT_PURPLE = '\033[94m'
C_PURPLE = '\033[95m'
C_END = '\033[0m'
C_BOLD = '\033[1m'
C_DIM = '\033[2m'
C_UND = '\033[4m'
C_BLINK = '\033[5m'
C_REV = '\033[7m'
C_HID = '\033[8m'

minval = (0, 0)
maxval = (0, 0)


class Datas():
    def __init__(self, file='data.csv'):
        self.data = []
        self.xlabel = ''
        self.ylabel = ''
        found_title = False
        with open(file) as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                if len(row) == 2:
                    if not found_title and not row[0].isnumeric():
                        self.xlabel, self.ylabel = row
                    elif row[0].isnumeric() and row[1].isnumeric():
                        self.data.append(list(map(int, row)))
                    found_title = True
        self.data.sort()
        self.__get_min_max__()

    def __get_min_max__(self):
        global minval, maxval
        valx, valy = zip(*self.data)
        minval = min(valx), min(valy)
        maxval = max(valx), max(valy)

    def plot(self, with_label=True):
        valx, valy = zip(*self.data)
        plt.plot(valx, valy, '+')
        if with_label:
            plt.xlabel(self.xlabel)
            plt.ylabel(self.ylabel)

    def debug(self):
        print(f'{C_DIM}Data:{C_END}', repr(self.data))

    def __repr__(self):
        return repr(self.data)


class Prediction(object):
    '''Prediction'''

    def __init__(self, teta0=0, teta1=0):
        self.teta0, self.teta1 = teta0, teta1

    def predict(self, mileage: int) -> int:
        print(self.data)
        return self.teta0 + (self.teta1 * mileage)

    def plot(self):
        x = np.linspace(minval[0], maxval[0], 100)
        y = self.teta1 * x + self.teta0
        plt.plot(x, y, '-r', label=f'y={self.teta1}x+{self.teta0}')
        plt.legend(loc='upper left')

    def debug(self):
        print(f'''\
teta0[{C_GREEN}{self.teta0}{C_END}], teta1[{C_GREEN}{self.teta1}{C_END}]\
''')


def lauchInFire(t0: float, t1: float):
    data = Datas()
    data.debug()
    data.plot()
    pred = Prediction(t0, t1)
    pred.plot()
    plt.grid()
    plt.show()


def test():
    data = Datas()
    data.debug()
    data.plot()
    pred = Prediction(9500, -.03)
    pred.debug()
    pred.plot()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    fire.Fire(test)
    # fire.Fire(lauchInFire)
