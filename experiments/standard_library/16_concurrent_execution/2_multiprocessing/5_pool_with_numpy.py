from multiprocessing import Pool
import time
import numpy as np
from numpy.typing import NDArray

"""
NB: attempting to use numpy to handle the 1 Billion Integers which require $GB
Map Reduce
    Map = Distribute processing to multiple cores
    Reduce = Combine processing results from multiple cores
"""


def square(numbers: NDArray):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


if __name__ == "__main__":
    start_time = time.time()
    pool = Pool(processes=4)
    size = 1000_000_000

    numbers = np.arange(size)

    squares = pool.map(square, [numbers])
    pool.close()
    pool.join()

    end_time = time.time()
    print(f"Pool Processing Time: {end_time - start_time}")

    start_time = time.time()

    sum = 0
    for n in numbers:
        sum += n * n
    end_time = time.time()
    print(f"Sequential Processing Time: {end_time - start_time}")
