import scipy.optimize as opt

ALL_NUM = 6309

flow = [
    330,
    487,
    618,
    498,
    350,
    364,
    353,
    283,
    428,
    497,
    546,
    525,
    408,
    238,
    268,
    81,
]

total = sum(flow)
ratio = []
for i in range(0, len(flow), 2):
    ratio.append((flow[i] + flow[i + 1]) / total * ALL_NUM)
# print(sum(ratio))


n = ratio[0]
C1 = .01
C2 = 7.129
C3 = 2
D = 27
w1 = .8
w2 = 1 - w1


def func1(k, n=ratio[7]):
    g1 = C1 * (120 / k) * n
    g2 = C2 * k * D - n * C3

    # return w1 * g1 + w2 * g2

    g1max = opt.minimize_scalar(lambda k: -(C1 * (120 / k) * n), bounds=(5, 25), method='bounded').x
    g1min = opt.minimize_scalar(lambda k: C1 * (120 / k) * n, bounds=(5, 25), method='bounded').x

    g2max = opt.minimize_scalar(lambda k: -(C2 * k * D - n * C3), bounds=(5, 25), method='bounded').x
    g2min = opt.minimize_scalar(lambda k: C2 * k * D - n * C3, bounds=(5, 25), method='bounded').x

    print(w1 * (g1 - g1min) / (g1max - g1min), w2 * (g2 - g2min) / (g2max - g2min))

    return w1 * (g1 - g1min) / (g1max - g1min) + w2 * (g2 - g2min) / (g2max - g2min)


 ret = opt.minimize_scalar(func1, bounds=(5, 25), method='bounded')
 print(ret)

import matplotlib.pyplot as plt
import numpy as np
n = ratio[0]
x = np.linspace(0, 25, 100)
y = w1 * C1 * (120 / x) * n + w2 * (C2 * x * D - n * C3)
plt.figure()
plt.plot(x, y)
plt.show()
