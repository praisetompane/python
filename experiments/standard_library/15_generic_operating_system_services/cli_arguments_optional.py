import argparse


def execute_operation(num_1, num_2, operation):
    match operation:
        case "+":
            return num_1 + num_2
        case "*":
            return num_1 * num_2
        case "-":
            return num_1 - num_2
        case "/":
            return num_1 / num_2


"""
Example usage:
python experiments/cli_arguments_optional.py --num_1 1 --num_2 4 --operation +
NB: No error handling is implemented for when parameters are not supplied
"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_1", help="First number.")
    parser.add_argument("--num_2", help="Second number.")
    parser.add_argument(
        "--operation",
        help="Operation to apply to arguments.",
        choices=["+", "*", "-", "/"],
    )

    args = parser.parse_args()

    print(
        f"Result: {execute_operation(int(args.num_1), int(args.num_2), args.operation)}"
    )
