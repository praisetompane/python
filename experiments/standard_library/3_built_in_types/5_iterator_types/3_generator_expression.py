if __name__ == "__main__":
    print(sum(i * i for i in range(10)))
    print(sum(j * j for j in range(10) if j % 2 == 0))

    # More explicit experiment that it is returning an iterator
    itr = (i * i for i in range(10))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
