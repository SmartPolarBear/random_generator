import numpy as np
import matplotlib.pyplot as plt
import math

import uniform_rand


def rayleigh(count: int, sigma: float):
    uni = uniform_rand.uniform_rand(count)
    for u in uni:
        yield math.sqrt(-2.0 * (sigma ** 2.0) * math.log(u, math.e))


if __name__ == "__main__":
    plt.hist(list(rayleigh(10000, 2)), 100)
    plt.show()
