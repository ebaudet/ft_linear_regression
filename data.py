# coding: utf-8
import csv
import matplotlib.pyplot as plt

from color import *
import globvar as g


class Datas():
    def __init__(self, file=None):
        self.data = []
        self.xlabel = ''
        self.ylabel = ''
        self.__read_csv_file__(file)
        self.__get_min_max__()

    def __read_csv_file__(self, file=None):
        '''Extract datas from csv file.'''
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
        '''Define the min/max value of the datas.'''
        valx, valy = zip(*self.data)
        g.minval = min(valx), min(valy)
        g.maxval = max(valx), max(valy)

    def plot(self, with_label=True):
        '''Print on the graph the datas points.'''
        valx, valy = zip(*self.data)
        plt.plot(valx, valy, '+')
        if with_label:
            plt.xlabel(self.xlabel)
            plt.ylabel(self.ylabel)

    def error_value(self, t0, t1):
        '''Return the error between the datas and the curve f(x)=t0+x*t1.'''
        error = 0
        for x, y in self.data:
            error += abs((t0 + (t1 * x)) - y)
        error /= len(self.data)
        return error

    def debug(self):
        '''Print the datas.'''
        print('{}Data:{}'.format(C_DIM, C_END), repr(self))

    def __repr__(self):
        return repr(self.data)
