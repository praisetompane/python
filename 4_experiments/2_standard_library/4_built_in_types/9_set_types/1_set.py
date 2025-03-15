# 1. Option 1 for construction
basket = {"orange", "apple", "mango", "apple", "orange"}
print("Notice duplicates are removed, because sets are UNORDERED and UNIQUE")
print(type(basket))
print(basket)

# NB: basket = {}, creates a dictionary and not a set. There must be at least one value.

# 2. Option 2 for construction
basket_2 = set()
basket_2.add("orange")
basket_2.add("mango")
basket_2.add("apple")
basket_2.add("orange")
print(type(basket_2))
print(basket_2)


# 3. Option 3 for construction with iterable

basket_3 = set([i for i in range(10)])
print(type(basket_3))
print(basket_3)


# 4. operations
print("operations")
lower_case_letters = set([chr(i) for i in range(97, 107)])
upper_case_letters = set([chr(i) for i in range(65, 75)])
print(f"{lower_case_letters = }")
print(f"{upper_case_letters = }")
print("a" in lower_case_letters)
print("A" in upper_case_letters)


x = {"a", "b", "c"}
y = {"a", "g", "h"}

print(f"Union {x = } and {y = } = {x|y}")
print(f"Intersection {x = } and {y = } = {x&y}")
print(f"Difference {x = } and {y = } = {x-y}")
print(f"Subset {x = } and {y = } = {x<y}")
