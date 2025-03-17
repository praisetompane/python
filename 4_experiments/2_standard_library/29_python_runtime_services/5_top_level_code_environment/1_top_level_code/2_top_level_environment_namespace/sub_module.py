import __main__


def print_entry_point_state():
    print(
        f"Printing a value set in __main__(i.e. top-level | entry-point) module. Value is {__main__.variable}")
