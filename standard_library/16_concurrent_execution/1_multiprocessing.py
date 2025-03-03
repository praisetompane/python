"""
def multiprocessing:
    - formal: ???

        - in words: ???

    - plain english: ???

    - intuition: threading API applied to processes.

    - properties: 
      - specification: https://docs.python.org/3.11/library/multiprocessing.html
      - implementation:
        - high level: https://github.com/python/cpython/tree/main/Lib/multiprocessing
        - low level c extension: https://github.com/python/cpython/tree/main/Lib/multiprocessing
    - examples: see below

    - use cases: ???

    - proof: None. It is a definition.

References: ???

"""

import multiprocessing

squares = []


def square(numbers):
    global squares
    for n in numbers:
        squares.append(n**n)
    print(f"In process squares: {squares}")


if __name__ == "__main__":
    numbers = [i for i in range(10)]
    p_1 = multiprocessing.Process(target=square, args=[numbers])
    p_1.start()
    p_1.join()
    print(f"In main method squares {squares}")
