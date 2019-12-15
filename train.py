#!/usr/bin/env python3
# coding: utf-8
import matplotlib.pyplot as plt
import argparse

from color import *
import predict as p
import data as d


class GradientDescent:
    def __init__(self, data, learning_rate=1e-2, iterations=10, t0=0, t1=0):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.t0 = t0
        self.t1 = t1
        self.D = data
        self.ndata = self.normalize_data(self.D.data)

    def normalize_data(self, data):
        '''Normalize the data to have them betwen 0 and 1.'''
        _x, _y = list(zip(*data))
        self.normalize = max(_x)
        normalize_data = [[x / self.normalize for x in _x],
                          [y / self.normalize for y in _y]]
        return normalize_data

    def pred(self, x):
        '''Return the prediction with the current θ0 and θ1 for a given x.'''
        return self.t0 + self.t1 * x

    def gradient(self):
        '''Gradient descent algorithm.'''
        error_list = []
        x, y = self.ndata
        rng = range(len(self.D.data))
        m = float(len(self.D.data))
        for _i in range(self.iterations):
            d0 = (-1 / m) * sum([y[i] - self.pred(x[i]) for i in rng])
            d1 = (-1 / m) * sum([(y[i] - self.pred(x[i])) * x[i] for i in rng])
            self.t0 -= self.learning_rate * d0
            self.t1 -= self.learning_rate * d1
            error_list.append(self.D.error_value(self.t0, self.t1))
        self.t0 *= self.normalize
        try:
            with open('thetas.csv', 'w') as f:
                f.write('{0},{1}\n'.format(self.t0, self.t1))
        except Exception:
            print('{red}/!\\ Cannot save thetas value in {}.{end}'
                  .format(repr('thetas.csv'), red=C_RED, end=C_END))
        return error_list

    def result(self):
        '''Print the theta0 and theta1 found.'''
        print('*** θ0 [{green}{}{end}], θ1 [{green}{}{end}] ***'
              .format(self.t0, self.t1, green=C_GREEN, end=C_END))


def argParseTrain():
    '''Parsing given arguments.'''
    parser = argparse.ArgumentParser(description="Train the model to found the"
                                     " best θ0 and θ1 to fit f(x) = θ0 + θ1x")
    parser.add_argument("-g", "--graph",
                        help="Show the graph", action="store_true")
    parser.add_argument("-f", "--file", help="Data file (default:data.csv)",
                        default="data.csv", type=argparse.FileType('r'))
    parser.add_argument("-l", "--learning_rate", help="Learning Rate "
                        "(default:0.1)", default=0.1, type=float)
    parser.add_argument("-i", "--iterations", help="How many iterations "
                        "(default:5000)", default=5000, type=int)
    parser.add_argument("-t0", help="Starting θ0 (default:0)",
                        default=0, type=float)
    parser.add_argument("-t1", help="Starting θ1 (default:0)",
                        default=0, type=float)
    parser.add_argument("-v", "--verbose", help="Verbose mode",
                        action="store_true")
    args = parser.parse_args()
    return args


def main():
    args = argParseTrain()
    print('Training for : {und}{}{end}'
          .format(args.file.name, und=C_UND, end=C_END))
    data = d.Datas(args.file)
    if args.verbose:
        print('len datas:', len(data.data))
        data.debug()
    GD = GradientDescent(data, iterations=args.iterations,
                         learning_rate=args.learning_rate, t0=args.t0,
                         t1=args.t1)
    error_list = GD.gradient()
    GD.result()
    if args.graph:
        plt.subplot(1, 2, 1)
        plt.plot(range(len(error_list)), error_list)
        plt.subplot(1, 2, 2)
        data.plot()
        pred = p.Prediction(GD.t0, GD.t1)
        pred.plot()
        plt.show()


if __name__ == '__main__':
    main()
