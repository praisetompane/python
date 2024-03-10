squares = []
for x in range(10):
    squares.append(x**2)

print(f"squares: ", end="")
for x in range(10):
    print(f"{x}^2, ", end="")
print("")
print(f"squares: {squares}")


squares = list(map(lambda x: x**2, range(10)))
print(f"squares: {squares}")

# This is the list comprehension version
# general form: [(expression). for clause. >= 0 for clause | if. )]
squares = [x**2 for x in range(10)]
print(f"squares: {squares}")

squares = [(x**2) for x in range(10)]
print(f"squares: {squares}")


# combinations
list_a = [x for x in range(10)]
list_b = [x for x in range(10)]

combinations = [(x, y) for x in list_a for y in list_b]
print(f"combinations: {combinations}")

odd_sum_combinations = [(x, y) for x in list_a for y in list_b if (x + y) % 2 != 0]
print(f"odd_sum_combinations: {odd_sum_combinations}")

print("all Integer points in 3D Cube, including endpoints")
x = int(input("x coordinate: "))
y = int(input("y coordinate: "))
z = int(input("z coordinate: "))

coordinates = [
    (i, j, k)
    for i in range(0, x + 1)
    for j in range(0, y + 1)
    for k in range(0, z + 1)
]
print(coordinates)
