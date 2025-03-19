from library import Base


class Derived(Base):
    """
    Observation: Base.foo is not implemented.
    """
    """
    # implementing this will fix the error as expected.
    def foo(self):
        return "foo"
    """


if __name__ == "__main__":
    c = Derived()

"""
References:
    Powell, J. 2017. What Does It Take To Be An Expert At Python. PyData
"""
