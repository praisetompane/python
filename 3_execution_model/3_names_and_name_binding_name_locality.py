import math
import inspect
# code block begins here
def factorial_nonlocal(number):
    result = 1
    for n in range(1, number + 1):
        result *= n

    def squareroot():
        nonlocal result
        print("locals of version using result as nonlocal: ")
        print(inspect.currentframe().f_locals)
        return math.sqrt(result)
        
    return (result, squareroot())

def factorial_closure(number):
    result = 1
    for n in range(1, number + 1):
        result *= n

    def squareroot():
        print("locals of closure version: ")
        print(inspect.currentframe().f_locals)
        return math.sqrt(result)
        
    return (result, squareroot())


def access_global():
    global gloabl_test
    print(gloabl_test) # print(global gloabl_test) is illegal

# code block ends here
    
# code block begins here
if __name__ == "__main__":
    gloabl_test = "I am from main scope"
    number = 4 #int(input("Please enter a number to compute a factorial: "))
    print(f"factorial of {number} is: {factorial_nonlocal(number)}")
    print("\n")
    print(f"factorial of {number} is: {factorial_closure(number)}")
    print("\n")
    access_global()
# code block ends here
