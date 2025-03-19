

class BaseMeta(type):
    """
        objective: Implements solution 3. metaclass.
        Features:
            - allows interception of construction of derived classes.
            - they have various data model methods yo can use.

    """

    def __new__(cls, name, basses, body):
        # print('Base.__meta__', cls, name, basses, body)
        if not 'foo' in body:
            raise TypeError("Missing `foo` method on a subclass")
        return super().__new__(cls, name, basses, body)


class Base(metaclass=BaseMeta):
    def foo(self):
        """
            Observation: user.py code might not implement `foo` and this code will break.
            Question:
                1. How do you as a library author ensure that user code implements this?
                    i.e. Enforce constraints on classes that Derive from Base


            """
        return self.foo()


"""
References:
    Powell, J. 2017. What Does It Take To Be An Expert At Python. PyData
"""
