from library import Base


assert hasattr(
    Base, 'foo'), f"Library code for Base has no `foo` method"


class Derived(Base):
    def foo(self):
        """"
        Observation: This could break if foo is not defined
        Question:
            1. How can prevent this failing before production environment?
                - Solution:
                    1. write test for bar method in unit tests
                    2. check that method exists and fail otherwise(i.e. enforce a constraint) using an assert, like above.
        """
        return self.foo()


if __name__ == "__main__":
    c = Derived()
    c.foo()


"""
References:
    Powell, J. 2017. What Does It Take To Be An Expert At Python. PyData
"""
