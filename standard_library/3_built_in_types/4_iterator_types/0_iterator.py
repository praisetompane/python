"""
  def iterator:
    - formal:
      - in words: an object that represents a stream of data.

    - properties:
      - forward and reserve traversal.
      - can only be traversed once.
    - plain english: ???

    - intuition: ???

    - properties: ???

    - examples: ???

    - use cases: ???
        
    - proof: None. It is a definition.
      
  References:
    PEP 234 – Iterators. https://peps.python.org/pep-0234/
"""

collection = [i for i in range(5)]

print("Forward Iteration with next(forward_iterator)")
forward_iterator = iter(collection)
print(f"Type: {type(forward_iterator)}")
print(f"Print next element {next(forward_iterator)}")
print(f"Print next element {next(forward_iterator)}")
print(f"Print next element {next(forward_iterator)}")
print(f"Print next element {next(forward_iterator)}")
print(f"Print next element {next(forward_iterator)}")
# print(f"Print next element {next(forward_iterator)}")
print("\n")

print("Forward Iteration with __next__")
forward_iterator_2 = iter(collection)
print(f"Print next element {forward_iterator_2.__next__()}")
print(f"Print next element {forward_iterator_2.__next__()}")
print(f"Print next element {forward_iterator_2.__next__()}")
print(f"Print next element {forward_iterator_2.__next__()}")
print(f"Print next element {forward_iterator_2.__next__()}")
# print(f"Print next element {forward_iterator)}")
print("\n")

print("Reverse Iteration")
reverse_iterator = reversed(collection)
print(f"Type: {type(forward_iterator)}")
print(f"Print next element {next(reverse_iterator)}")
print(f"Print next element {next(reverse_iterator)}")
print(f"Print next element {next(reverse_iterator)}")
print(f"Print next element {next(reverse_iterator)}")
print(f"Print next element {next(reverse_iterator)}")
# print(f"Print next element {next(reverse_iterator)}")
print("\n")

# Single Travel Example
collection = [i for i in range(5)]
iterator = iter(collection)

print("First pass of the iterator")
for v in iterator:
    print(v)

# This next pass will fail, because we have exhausted the iterator's single pass
print("Second pass of the iterator")
for v in iterator:
    print(v)
