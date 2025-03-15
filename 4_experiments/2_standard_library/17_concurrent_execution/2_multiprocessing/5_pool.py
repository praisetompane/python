import multiprocessing
from multiprocessing import Pool
import time


"""
Map Reduce
    Map = Distribute processing to multiple cores
    Reduce = Combine processing results from multiple cores
"""


def square(numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


if __name__ == "__main__":
    start_time = time.time()
    pool = Pool(processes=4)
    size = 1000_000
    numbers = [i for i in range(size)]

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
