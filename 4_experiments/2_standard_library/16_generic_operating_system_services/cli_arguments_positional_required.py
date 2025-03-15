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
Example Usage:
python experiments/cli_arguments_positional_required.py 1 4 + 
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("num_1", help="first numeric operand")
    parser.add_argument("num_2", help="second numeric operand")
    parser.add_argument(
        "operation",
        help="operation to perform on the two numbers",
        choices=["+", "*", "-", "/"],
    )

    args = parser.parse_args()

    print(
        f"result = {execute_operation(int(args.num_1), int(args.num_2), args.operation)}"
    )
