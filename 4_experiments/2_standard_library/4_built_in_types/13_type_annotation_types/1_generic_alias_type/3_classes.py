class IntToIntOrStringDictionary[int, T: (int | str)]:

    def __init__(self,) -> None:
        self.values: dict[int, T] = {}

    def add(self, key: int, value: T):
        self.values[key] = value

    def __repr__(self):
        return ",".join(f"{k}:{v}" for k, v in self.values.items())


if __name__ == "__main__":
    v = IntToIntOrStringDictionary()
    v.add(1, "a")
    v.add(2, 1)
    print((type(v)))
    print((type(v.values)))
    print(v)
