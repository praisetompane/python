"""
  def iter: construct to traverse an arbitrary data structure
    - properties:
      - forward and reserve traversal
"""

collection = [i for i in range(5)]

print("Forward Iteration")
forward_iterator = iter(collection)
print(f"Print next element {next(forward_iterator)}")
print(f"Print next element {next(forward_iterator)}")
print(f"Print next element {next(forward_iterator)}")
print(f"Print next element {next(forward_iterator)}")
print(f"Print next element {next(forward_iterator)}")
# print(f"Print next element {next(forward_iterator)}")

print("Reverse Iteration")
reverse_iterator = reversed(collection)
print(f"Print next element {next(reverse_iterator)}")
print(f"Print next element {next(reverse_iterator)}")
print(f"Print next element {next(reverse_iterator)}")
print(f"Print next element {next(reverse_iterator)}")
print(f"Print next element {next(reverse_iterator)}")
# print(f"Print next element {next(reverse_iterator)}")

print(dir(collection))
