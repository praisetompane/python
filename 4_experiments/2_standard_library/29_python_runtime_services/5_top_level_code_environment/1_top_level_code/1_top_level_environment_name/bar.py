from foo import foo


def bar():
    print("In bar function")
    print(f"top-level code module: {__name__}")
    foo()


if __name__ == "__main__":
    print("In bar module, as top-level code environment")
    bar()
