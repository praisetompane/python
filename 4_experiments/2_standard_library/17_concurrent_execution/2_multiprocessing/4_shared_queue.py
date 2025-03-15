import multiprocessing


def square(numbers, squares):
    for n in numbers:
        squares.put(n * n)
    print(f"In second process {squares}")


if __name__ == "__main__":
    size = 10
    nums = [i for i in range(size)]
    squares = multiprocessing.Queue()
    p_1 = multiprocessing.Process(target=square, args=(nums, squares))

    p_1.start()
    p_1.join()
    print(f"In fist process {squares}")
    while not squares.empty():
        print(f"{squares.qsize() = }")
        print(squares.get())
