"""
def decorators:
    - formal: 𝑓: 𝑓 ↦ Modified[𝑓]

        - in words: a high order function to modify and execute functions/methods

    - plain english: syntactic sugar for invoking a high order function directly and returning the parameter function's result.

    - intuition: ???

    - properties:
      - specification: https://peps.python.org/pep-0318/

    - examples:
      - see function runtime tracker below: def timed

    - use cases:
      - aspect orientated programming:
        - logging

    - proof: ???

References: ???
"""

import time


def timed(func):
    def function_executor(*args, **kwargs):
        print(f"Executing Function: {func.__name__} ")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(
            f"Function: {func.__name__} took {(end - start)*1000} miliseconds to complete."
        )
        return result

    return function_executor


@timed
def square(numbers):
    result = []
    for num in numbers:
        result.append(num * num)
    return result


@timed
def square_map_implementation(numbers):
    return list(map(lambda i: i * i, numbers))


if __name__ == "__main__":
    numbers = [i for i in range(10)]
    print(square(numbers))
    print(square_map_implementation(numbers))

    # direct invocation
    square_decorated = timed(square)
    print(square_decorated(numbers))
