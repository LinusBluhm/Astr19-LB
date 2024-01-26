import numpy as np
from tabulate import tabulate


def main():
    x = np.linspace(0, 2*np.pi, 1000)
    y = np.sin(x)

    sin_tuples = [(a,b) for a,b in zip(x,y)]
    print(tabulate(sin_tuples, tablefmt="grid", headers=['x', 'y'], floatfmt=".4f"))


main()
