#!/usr/bin/env python3
# coding: utf-8
import csv
import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal as D
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
        self.__read_csv_file__(file)
        self.__get_min_max__()

    def __read_csv_file__(self, file='data.csv'):
        found_labels = False
        try:
            with open(file) as csvfile:
                for row in csv.reader(csvfile, delimiter=','):
                    if len(row) == 2:
                        try:
                            valx, valy = list(map(float, row))
                            self.data.append(list((valx, valy)))
                        except ValueError:
                            if not found_labels:
                                self.xlabel, self.ylabel = row
                        found_labels = True
        except Exception:
            print(f'{C_RED}No data to train to.{C_END}')
            quit()
        self.data.sort()

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

    def error_value(self, t0, t1):
        '''Calculate the error'''
        error = 0
        for x, y in self.data:
            error += (t0 + (t1 * x)) - y
        error /= len(self.data)
        return error

    def debug(self):
        print(f'{C_DIM}Data:{C_END}', repr(self.data))

    def __repr__(self):
        return repr(self.data)


class Prediction(object):
    '''Prediction'''

    def __init__(self, t0=0, t1=0):
        self.__read_from_file__(t0, t1)

    def __read_from_file__(self, t0, t1):
        try:
            with open('thetas.csv') as thetas_file:
                for row in csv.reader(thetas_file, delimiter=','):
                    if len(row) == 2:
                        _t0, _t1 = list(map(float, row))
                        self.t0, self.t1 = _t0, _t1
                    break
        except Exception:
            self.t0, self.t1 = t0, t1


    def predict(self, mileage: int) -> int:
        return self.t0 + (self.t1 * mileage)

    def plot(self):
        x = np.linspace(minval[0], maxval[0], 100)
        y = self.t1 * x + self.t0
        plt.plot(x, y, '-r', label=f'y={self.t1}x+{self.t0}')
        plt.legend(loc='upper left')

    def predict_price(self, data, error_calculated):
        while True:
            try:
                input_val = input("Enter mileage number, or 'graph' to"
                                  " visualize or 'q' to quit\n> ")
                if input_val in ('q', 'Q', 'quit'):
                    return
                if input_val in ('g', 'G', 'graph'):
                    graph(data, self, error_calculated)
                    continue
                x = float(input_val)
                print(f"For {C_UND}{x}km{C_END}, estimate price is "
                      f"{C_PURPLE}${round(self.t0+self.t1*x, 2)}{C_END}")
            except ValueError:
                print('Oops! That as no a valid number. Try again...')
            except EOFError:
                print()
                return()

    def debug(self):
        print(f'''\
*** θ0 [{C_GREEN}{self.t0}{C_END}], θ1 [{C_GREEN}{self.t1}{C_END}] ***\
''')


def graph(data, pred, error_calculated):
    data.plot()
    pred.plot()
    plt.title(f'Error : {error_calculated}')
    plt.grid()
    plt.show()


def lauchInFire(t0: float, t1: float, file=None):
    data = Datas(file)
    print('len:', len(data.data))
    data.debug()
    pred = Prediction(t0, t1)
    pred.debug()
    error_calculated = data.error_value(pred.t0, pred.t1)
    print(f'*** error calculated: {C_GREEN}{error_calculated}{C_END} ***')
    pred.predict_price(data, error_calculated)


def test():
    lauchInFire(9500, -.03, 'data.csv')
    lauchInFire(0, 2, 'test.csv')


if __name__ == '__main__':
    fire.Fire(test)
    # fire.Fire(lauchInFire)
