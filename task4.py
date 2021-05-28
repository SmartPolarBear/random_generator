import matplotlib.figure
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import math

import uniform_rand


def random(count: int):
    us = uniform_rand.uniform_rand(count)

    for u in us:
        if u < 0.2:
            yield 1
        elif u < 0.35:
            yield 2
        elif u < 0.6:
            yield 3
        else:
            yield 4


if __name__ == "__main__":
    x = list(random(100000))
    weights = np.ones_like(x) / float(len(x))
    p = plt.hist(x,
                 bins=4,
                 normed=False,
                 weights=weights,
                 histtype='stepfilled',
                 color=[0.1, 0.4, 0.3]
                 )

    plt.ylim(0, 1)
    plt.show()
