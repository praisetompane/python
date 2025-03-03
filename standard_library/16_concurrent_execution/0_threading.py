"""
def thread:
    - formal: ???

        - in words: ???

    - plain english: ???

    - intuition: ???

    - properties:
        - specification: 
            - high level: https://docs.python.org/3.11/library/threading.html
            - low level: https://docs.python.org/3.11/library/_thread.html#module-_thread
        - constraints:
            - CPython: Due to the Global Interpreter Lock(GIL), only one thread can execute python code at a time.
            - threading module not available on WebAssembly platforms(i.e. wasm32-emscripten, wasm32-wasi).
    - examples: ???

    - use cases:
        - multiple IO bound tasks
        
    - proof: ???
    
References: ???

"""

import threading


def square(numbers):
    for x in numbers:
        squares.append(x * x)


def cube(numbers):
    for x in numbers:
        cubes.append(x * x * x)


if __name__ == "__main__":
    numbers = [i for i in range(10)]
    squares = []
    cubes = []

    t_1 = threading.Thread(target=square, args=[numbers])
    t_2 = threading.Thread(target=cube, args=[numbers])

    t_1.start()
    t_2.start()

    t_1.join()
    t_2.join()

    print(squares)
    print(cubes)
