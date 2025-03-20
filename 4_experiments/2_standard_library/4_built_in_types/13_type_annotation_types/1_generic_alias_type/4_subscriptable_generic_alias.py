from typing import TypeVar

"""
dict[int][int] fails, because dict[int] returns a GenericAlias, which is not subscriptable.
"""
try:
    a = dict[int][int]
    print(type(a))
except TypeError as e:
    print("Expected Error")
    print(f"{e} \n")


print("subscriptable if TypeVar is used to create the Type Variable\n")
print("Notice the second type parameter is ~T")
T = TypeVar("T")
d = dict[int, T]

print(d)

print("Subscripting `d`` to create dict[int, str]\n")
dict_int_to_str = d[str]

print(dict_int_to_str)
print(type(dict_int_to_str))
