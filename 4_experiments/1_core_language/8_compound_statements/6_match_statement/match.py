print("as a switch statement")
options = ["a", "b", "c"]
v = input("Please provide letter: ")

match v:
    case "a":
        print("found something I `am looking for")
    case __:
        print("did not find value i know how to use use")


print("structural pattern matching")
foo = (1, 1)
foo_t = tuple(foo)
print(foo_t)

match foo_t:
    case (a, b):
        print("found something I `am looking for")
    case _:
        print("did not find value i know how to use use")
