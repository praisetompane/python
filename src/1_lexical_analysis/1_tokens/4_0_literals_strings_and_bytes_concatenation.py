import re


print("""example syntactic level string concatenation
      notice that the individual strings are implicitly concatenated into one""")

match = re.compile(
    "[A-Za-z_]" "[A-Za-z0-9_]*"  # letter or underscore  # letter, digit or underscore
)

print(match.pattern)

bar = 1
foo = "double quote" "single quote" """triple double quote""" f"a formatted string {bar}" r"a raw string"
print(repr(foo))

print("example where '+' is required for runtime concatenation")
foo = ""
for i in range(0, 10):
    #foo str(i) # this is illegal, we must use + at runtime
    foo += str(i)
print(foo)

print("example byte concatenation")
byte_example = b"00000001" + b"00000000"
print(byte_example)