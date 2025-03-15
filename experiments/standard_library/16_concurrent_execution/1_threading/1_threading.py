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
