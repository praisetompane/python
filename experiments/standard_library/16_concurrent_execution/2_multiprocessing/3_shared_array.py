import multiprocessing


def square(numbers, squares):
    for idx, x in enumerate(numbers):
        num_squared = x * x
        squares[idx] = num_squared
    print(f"In second process: {list(squares)}")


if __name__ == "__main__":
    size = 10
    nums = [i for i in range(size)]
    squares = multiprocessing.Array("i", size)
    p_1 = multiprocessing.Process(target=square, args=(nums, squares))

    p_1.start()
    p_1.join()
    print(f"In first process: {squares[:]}")
