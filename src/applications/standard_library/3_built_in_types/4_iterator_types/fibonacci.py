def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a = b
        b = a + b


for n in fibonacci():
    if n > 50:
        break
    print(n)
