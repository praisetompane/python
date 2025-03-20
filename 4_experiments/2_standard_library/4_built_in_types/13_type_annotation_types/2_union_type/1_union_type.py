from types import UnionType
from typing import Optional
# clean syntac for typing.Union

print("Type of int | str")
print(type(int | str))


print("Optional type")
d = int | None
print(type(d))

print("Test equivalence to Optional[int]")
assert d == Optional[int]


print(isinstance(d, UnionType))
