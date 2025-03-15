import multiprocessing


def square(numbers, squares, sum):
    for idx, x in enumerate(numbers):
        num_squared = x * x
        squares[idx] = num_squared
        sum.value += num_squared

    print(f"Sum in second process {sum.value}")


if __name__ == "__main__":
    size = 10
    nums = [i for i in range(size)]
    squares = multiprocessing.Array("i", size)
    sum = multiprocessing.Value("i")
    p_1 = multiprocessing.Process(target=square, args=(nums, squares, sum))

    p_1.start()
    p_1.join()
    print(f"Sum in first process {sum.value}")
