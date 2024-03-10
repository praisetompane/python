import fileinput

with fileinput.input(files="0_stdio_file_text_test.txt") as f:
    for line in f:
        print(line)
