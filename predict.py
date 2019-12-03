#!/usr/bin/env python3
# coding: utf-8
import csv
import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal as D
import argparse

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
    def __init__(self, file=None):
        self.data = []
        self.xlabel = ''
        self.ylabel = ''
        self.__read_csv_file__(file)
        self.__get_min_max__()

    def __read_csv_file__(self, file=None):
        found_labels = False
        try:
            with file as csvfile:
                for row in csv.reader(csvfile, delimiter=','):
                    if len(row) == 2:
                        try:
                            valx, valy = list(map(float, row))
                            self.data.append(list((valx, valy)))
                        except ValueError:
                            if not found_labels:
                                self.xlabel, self.ylabel = row
                        found_labels = True
            if len(self.data) == 0:
                raise Exception
        except Exception:
            print('{red}No data to train to.{end}'
                  .format(red=C_RED, end=C_END))
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
            error += abs((t0 + (t1 * x)) - y)
        error /= len(self.data)
        return error

    def debug(self):
        print('{}Data:{}'.format(C_DIM, C_END), repr(self.data))

    def __repr__(self):
        return repr(self.data)


class Prediction(object):
    '''Prediction'''

    def __init__(self, t0=None, t1=None):
        self.t0, self.t1 = 0, 0
        self.__read_from_file__(t0, t1)

    def __read_from_file__(self, t0, t1):
        if t0 is not None and t1 is not None:
            self.t0, self.t1 = t0, t1
            return
        try:
            with open('thetas.csv') as thetas_file:
                for row in csv.reader(thetas_file, delimiter=','):
                    if len(row) == 2:
                        _t0, _t1 = list(map(float, row))
                        self.t0, self.t1 = _t0, _t1
                    break
        except Exception:
            pass
        if t0 is not None:
            self.t0 = t0
        if t1 is not None:
            self.t1 = t1

    def predict(self, mileage):
        return self.t0 + (self.t1 * mileage)

    def plot(self):
        x = np.linspace(minval[0], maxval[0], 100)
        y = self.t1 * x + self.t0
        plt.plot(x, y, '-r', label='y={}+{}x'.format(self.t0, self.t1))
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
                print("For {und}{}km{end}, estimate price is "
                      "{purple}${}{end}"
                      .format(x, round(self.t0 + self.t1 * x, 2), und=C_UND,
                              end=C_END, purple=C_PURPLE))
            except ValueError:
                print('Oops! That as no a valid number. Try again...')
            except EOFError:
                print()
                return()

    def debug(self):
        print('*** θ0 [{green}{}{end}], θ1 [{green}{}{end}] ***'
              .format(self.t0, self.t1, green=C_GREEN, end=C_END))


def graph(data, pred, error_calculated):
    data.plot()
    pred.plot()
    plt.title('Error : {}'.format(error_calculated))
    plt.grid()
    plt.show()


def lauchInFire(args, t0=None, t1=None, file=None):
    data = Datas(file)
    if args.verbose:
        print('len data:', len(data.data))
        data.debug()
    pred = Prediction(t0, t1)
    pred.debug()
    error_calculated = data.error_value(pred.t0, pred.t1)
    print('*** error calculated: {}{}{} ***'
          .format(C_GREEN, error_calculated, C_END))
    pred.predict_price(data, error_calculated)


def argParsePredict():
    parser = argparse.ArgumentParser(description="Predict the price for a "
                                     "given mileage")
    parser.add_argument("-f", "--file", help="Data file (default:data.csv)",
                        default="data.csv", type=argparse.FileType('r'))
    parser.add_argument("-t0", help="θ0: if not specified, take the one found "
                        "by train.py.", default=None, type=float)
    parser.add_argument("-t1", help="θ1: if not specified, take the one found "
                        "by train.py.", default=None, type=float)
    parser.add_argument("-v", "--verbose", help="Verbose mode",
                        action="store_true")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    try:
        args = argParsePredict()
        print('Predict from : {und}{}{end}'
              .format(args.file.name, und=C_UND, end=C_END))
        lauchInFire(args, args.t0, args.t1, args.file)
    except KeyboardInterrupt:
        pass
