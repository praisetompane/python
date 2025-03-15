def generate_infinite_numbers():
    """
    Generate infinite numbers
    """
    number = 0
    while True:
        yield number
        number += 1


def generator_expression():
    sum(i * i for i in range(10))


if __name__ == "__main__":
    last_number = 100
    print(f"Generating a {last_number} numbers")
    for number in generate_infinite_numbers():
        print(number)

    print(generator_expression)
