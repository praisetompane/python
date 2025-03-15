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
