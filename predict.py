#!/usr/bin/env python3
# coding: utf-8
import csv
import matplotlib.pyplot as plt
import numpy as np
import argparse

from color import *
import globals as g
import data as d


class Prediction(object):
    '''Prediction'''

    def __init__(self, t0=None, t1=None):
        self.t0, self.t1 = 0, 0
        self.__read_from_file__(t0, t1)

    def __read_from_file__(self, t0, t1):
        '''Define t0 and t1 according to trained data in thetas.csv.'''
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
        '''Return the predicted price for the given mileage

        (price = θ0 + θ1 * mileage).
        '''
        return self.t0 + (self.t1 * mileage)

    def plot(self):
        '''Print on the graph the predicted curve.'''
        x = np.linspace(g.minval[0], g.maxval[0], 100)
        y = self.predict(x)
        plt.plot(x, y, '-r', label='y={}+{}x'.format(self.t0, self.t1))
        plt.legend(loc='upper left')

    def prompt(self, data, error_calculated):
        '''Prompt the preduction.'''
        while True:
            try:
                input_val = input("Enter mileage value, or 'graph' to"
                                  " visualize or 'q' to quit\n> ")
                if input_val in ('q', 'Q', 'quit'):
                    return
                if input_val in ('g', 'G', 'graph'):
                    graph(data, self, error_calculated)
                    continue
                x = float(input_val)
                self.predict_price(x)
            except ValueError:
                print('Oops! That as no a valid number. Try again...')
            except EOFError:
                print()
                return()

    def predict_price(self, km):
        '''Print the predicted price for the given km.'''
        print("For {und}{}km{end}, estimate price is "
              "{purple}${}{end}"
              .format(km, round(self.predict(km), 2), und=C_UND,
                      end=C_END, purple=C_PURPLE))

    def debug(self):
        print('*** θ0 [{green}{}{end}], θ1 [{green}{}{end}] ***'
              .format(self.t0, self.t1, green=C_GREEN, end=C_END))


def graph(data, pred, error_calculated):
    data.plot()
    pred.plot()
    plt.title('Error : {}'.format(error_calculated))
    plt.grid()
    plt.show()


def main(args, t0=None, t1=None, file=None):
    data = d.Datas(file)
    if args.verbose:
        print('len data:', len(data.data))
        data.debug()
    pred = Prediction(t0, t1)
    pred.debug()
    error_calculated = data.error_value(pred.t0, pred.t1)
    print('*** error calculated: {}{}{} ***'
          .format(C_GREEN, error_calculated, C_END))
    pred.prompt(data, error_calculated)


def argParsePredict():
    '''Parsing given arguments.'''
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
        main(args, args.t0, args.t1, args.file)
    except KeyboardInterrupt:
        print('\nSee you later')
        pass
