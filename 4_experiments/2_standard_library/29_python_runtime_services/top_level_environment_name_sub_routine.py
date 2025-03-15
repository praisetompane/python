from top_level_environment_name import foo


def bar():
    print("In bar")
    print(f"{__name__ = }")
    foo()


if __name__ == "__main__":
    bar()
