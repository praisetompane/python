# code block begins here
def factorial(number):
    result = 1
    for n in range(1, number+1):
        result *= n
    return result
# code block ends here

# code block begins here
if __name__ == "__main__":
    number = int(input("Please enter a number to compute a factorial: "))
    print(f"factorial of {number} is: {factorial(number)}")
# code block ends here