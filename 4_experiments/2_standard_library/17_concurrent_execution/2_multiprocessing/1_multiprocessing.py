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
