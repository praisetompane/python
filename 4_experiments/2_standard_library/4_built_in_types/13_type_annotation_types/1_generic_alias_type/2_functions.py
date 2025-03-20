from collections.abc import Sequence
from typing import TypeVar


def generic_function_type_parameter[T](values: Sequence[T]):
    return values[0]


def generic_function_bound_type_parameter[T: int](values: Sequence[T]):
    return values[3]


TypeVariable = TypeVar("TypeVariable")
def independently_defined_type_variable(values: Sequence[TypeVariable]):
    return values[1]


BoundTypeVariable = TypeVar("BoundTypeVariable", bound=float)
def independently_defined_and_bound_type_variable(values: Sequence[BoundTypeVariable]):
    return values[2]


if __name__ == "__main__":
    values = [2, 4, 6, 8]
    print(generic_function_type_parameter(values))
    print(independently_defined_type_variable(values))
    float_values = [2.0, 2.1, 4.5, 5.6]
    print(independently_defined_and_bound_type_variable(float_values))
    print(generic_function_bound_type_parameter(values))
