#!/usr/bin/env python3
# coding: utf-8

import predict as p


class Exemple:
    def __init__(self):
        self.next_x = 6  # We start the search at x=6
        self.gamma = 0.01  # Step size multiplier
        self.precision = 1e-5  # Desired precision of result
        self.max_iters = 1000  # Maximum number of iterations

    def df(self, x):
        '''Derivative function'''
        return 4 * x**3 - 9 * x**2

    def gradient(self):
        for _i in range(self.max_iters):
            current_x = self.next_x
            self.next_x = current_x - self.gamma * self.df(current_x)

            step = self.next_x - current_x
            if abs(step) <= self.precision:
                break
        return self.next_x


class GradientDescent:
    def __init__(self, data, learning_rate=0.1, precision=1e-5,
                 max_iters=10, t0=0, t1=0):
        self.learning_rate, self.precision = learning_rate, precision
        self.max_iters, self.t0, self.t1 = max_iters, t0, t1
        self.data = data

    def step_gradient(self, t0, t1):
        tmpt0, tmpt1 = 0, 0
        for x, y in self.data.data:
            tmpt0 += -(2 / len(self.data.data) * (y - (t1 + x) + t0))
            tmpt1 += -(2 / len(self.data.data) * x * (y - (t1 + x) + t0))
        t0 -= self.learning_rate * tmpt0
        t1 -= self.learning_rate * tmpt1
        return t0, t1

    def gradient(self):
        for _i in range(self.max_iters):
            t0, t1 = self.step_gradient(self.t0, self.t1)
            step = self.t0 - t0
            self.t0, self.t1 = t0, t1
            if abs(step) <= self.precision:
                break
        return self.t0, self.t1


def main():
    data = p.Datas('data.csv')
    GD = GradientDescent(data)
    GD.gradient()
    print(f't0 : {GD.t0}, t1 : {GD.t1}')


if __name__ == '__main__':
    main()
