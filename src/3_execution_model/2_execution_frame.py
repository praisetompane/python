import inspect  # allows inspecting running code to extract frames and other useful introspection data


# code block begins here
def factorial(number):
    factorial_frame = inspect.currentframe()
    print(f"execution frame for factorial function: {factorial_frame}\n")

    print("factorial function code in frame:")
    print(factorial_frame.f_code)
    print("\n")

    print("local names at beginning of function: ")
    print(factorial_frame.f_locals)
    print("\n")

    print("outer frame from factorial function's frame: ")
    print(factorial_frame.f_back)
    print("Q: Is this where to go next after the current frame?")
    print("\n")

    result = 1
    for n in range(1, number + 1):
        result *= n

    print("local names at end of function: ")
    print(factorial_frame.f_locals)

    print("\n")
    return result


# code block ends here

# code block begins here
if __name__ == "__main__":
    number = 4  # int(input("Please enter a number to compute a factorial: "))
    print(f"execution frame for the module invoked as main: {inspect.currentframe()}\n")
    print(f"factorial of {number} is: {factorial(number)}")
    print("more code")
# code block ends here
