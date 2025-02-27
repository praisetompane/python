"""    
  def generator | generator function: 
    - formal: 𝑓: * ↦ Generator Iterator
        - in words: a function that creates and returns a Generator Iterator.

    - plain english: ???

    - intuition: ???

    - properties: ???

    - examples:
      - useful example: src/applications/math/fibonacci.py

    - use cases:
      - process or generate N values without using up N memory. Especially useful when N is large or even greater than all available memory.
      - Just In Time processing: generate values as they become available and process them at call/client side.
        
    - proof: None. It is a definition.
      
  References:
    PEP 255 – Simple Generators. https://www.python.org/dev/peps/pep-0255/#motivation

"""


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
