#!/usr/bin/env python3
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.01, 5.0, 0.01)


def linear(teta0, teta1, t):
    return (t, teta0 + (teta1 * t))


plt.title('data')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.plot(linear(0, 0.5, t))
plt.show()
