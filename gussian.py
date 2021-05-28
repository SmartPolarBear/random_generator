import numpy as np
import matplotlib.pyplot as plt
import math
import enum

import uniform_rand
import rayleigh


class Type(enum.Enum):
    HOMOPHASE = 1
    ORTHOGONAL = 2


def gaussian(count: int, sigma: float, t: Type):
    uniforms = uniform_rand.uniform_rand(count)
    rayleighs = rayleigh.rayleigh(count, sigma)

    trans = math.sin if t == Type.ORTHOGONAL else math.cos

    for u in uniforms:
        yield rayleighs.__next__() * trans(2 * math.pi * u)


if __name__ == "__main__":
    plt.hist(list(gaussian(1000000, 4, Type.ORTHOGONAL)), 100)
    plt.show()
