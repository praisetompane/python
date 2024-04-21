""" 
generic flow:

print("headline")
value = type_conversion_function(input("prompt: "))
# do stuff
print(value) 
"""

import builtins

# example


def extract_input(
    input_prompt: str, value_type: builtins, collection_type: builtins = None
):
    values = input(input_prompt).split()
    if collection_type is not None:
        return collection_type(map(value_type, values))
    else:
        return values


print("Please enter two numbers on separate lines")
num_one = int(input("Please enter number: "))
num_two = int(input("Please enter number: "))
print(f"sum: {num_one + num_two}")
integer_list_input = list(
    map(int, input("Please enter a space separated list of numbers:").split())
)
print(f"numbers inputted: {integer_list_input}")

items_list_input = extract_input(
    "Generic please enter a space separated list of numbers: ", int, list
)
print(f"numbers inputted: {items_list_input}")
