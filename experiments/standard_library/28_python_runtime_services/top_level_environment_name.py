"""
top level code is also called the entry-point.
"""


def foo():
    print("In foo")
    print(f"{__name__ = }")


if __name__ == "__main__":
    foo()
