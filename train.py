#!/usr/bin/env python3
# coding: utf-8
import matplotlib.pyplot as plt
import predict as p


class GradientDescent:
    def __init__(self, data, learning_rate=1e-2, max_iters=10, t0=0, t1=0,
                 scale=1000):
        self.learning_rate = learning_rate
        self.max_iters = max_iters
        self.t0 = t0
        self.t1 = t1
        self.D = data
        self.sdata = self.scale_data(self.D.data, scale)

    def scale_data(self, data, scale):
        scaled_data = []
        for x, y in data:
            scaled_data.append((x / scale, y / scale))
        return scaled_data

    def pred(self, x):
        return self.t0 + self.t1 * x

    def gradient(self):
        error_list = []
        x, y = list(zip(*self.sdata))
        rng = range(len(self.D.data))
        m = float(len(self.D.data))
        for _i in range(self.max_iters):
            d0 = (-1 / m) * sum([y[i] - self.pred(x[i]) for i in rng])
            d1 = (-1 / m) * sum([(y[i] - self.pred(x[i])) * x[i] for i in rng])
            self.t0 -= self.learning_rate * d0
            self.t1 -= self.learning_rate * d1
            error_list.append(self.D.error_value(self.t0, self.t1))
        return error_list


def main():
    data = p.Datas('data.csv')
    print('len:', len(data.data))
    GD = GradientDescent(data, max_iters=300000,
                         learning_rate=0.0001, t0=0, t1=0, scale=1000)
    print(GD.sdata)
    error_list = GD.gradient()
    print(f't0 : {GD.t0}, t1 : {GD.t1}')
    plt.plot(range(len(error_list)), error_list)
    plt.show()


if __name__ == '__main__':
    main()
