print("Examples overriding file content and creating non existing file")
file = open("./experiments/files_override.data", "w+")
file.write("I love Programming\n")
file.writelines(["I love Mathematics\n", "I love logic\n"])

print("Examples appending file content and creating non existing file")
file = open("./experiments/files_append.data", "a+")
file.write("I love Programming\n")
file.writelines(["I love Mathematics\n", "I love logic\n"])


print(
    "Examples reading existing file, counting words in lines and appending count to each line"
)
source = open("./experiments/files_override.data", "r")
target = open("./experiments/files_append_count.data", "a+")
target.truncate(0)
for l in source.readlines():
    line_stripped = l.strip("\n")
    target.write(f"{line_stripped}. {len(l.split(' '))} words.\n")
target.close()

print("Example of safe file processing")
with open("./experiments/files_append_count.data", "r") as file:
    for l in file.readlines():
        print(l)
    # auto closes the file

print("Example of opening non-existent file")
try:
    with open("./experiments/files_not_exist.data", "r") as file:
        for l in file.readlines():
            print(l)
        # auto closes the file

except FileNotFoundError as e:
    print(f"Error: Could not file file. Exception: {e}")
