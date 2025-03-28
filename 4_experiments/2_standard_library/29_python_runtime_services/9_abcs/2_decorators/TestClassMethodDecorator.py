import abc
from abc import abstractmethod

class TestClassMethodDecorator():
    @staticmethod
    def method_static_method():
        print("In static method")

    @classmethod    
    def method_class_method(cls):
        print("In class method")

    @abstractmethod
    def method_abstract(self):
        print("In abstract method")

    @staticmethod
    @abstractmethod
    def method_abstract_static():
        print("In abstract static method")

    def invoke_method_static_method_in_class(self):
        """
        Q: why can't we do this?
        """
        method_static_method()


if __name__ == "__main__":
    print(f"Test: {TestClassMethodDecorator.__name__}")
    a = TestClassMethodDecorator()
    a.method_static_method()
    TestClassMethodDecorator.method_static_method()
    # a.invoke_method_static_method_in_class()

    a.method_abstract()
    # TestClassMethodDecorator.method_abstract()
    TestClassMethodDecorator.method_abstract_static()
    
    a.method_class_method()
    TestClassMethodDecorator.method_class_method()

    print(abc.get_cache_token())
    print(type(abc.get_cache_token()))