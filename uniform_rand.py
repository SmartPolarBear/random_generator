import time

import numpy as np
import matplotlib.pyplot as plt

x: float = time.time()
y: float = time.time()
z: float = time.time()


def uniform_rand(count: int):
    for g in range(count):
        global x, y, z
        x = 171 * x % 30269
        y = 170 * y % 30307
        z = 172 * z % 30323

        yield (x / 30269 + y / 30307 + z / 30323) % 1


if __name__ == "__main__":
    gx: list = list(uniform_rand(1000))
    gy: list = list(uniform_rand(1000))

    plt.scatter(gx, gy, alpha=0.8)
    plt.show()
