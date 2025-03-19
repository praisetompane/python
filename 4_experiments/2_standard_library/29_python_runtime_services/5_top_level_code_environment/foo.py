"""
top level code is also called the entry-point.
"""


def foo():
    print("In foo function")
    print(f"top-level code module: {__name__}")


if __name__ == "__main__":
    print("In foo module, as top-level code environment")
    foo()
