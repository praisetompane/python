"""
  divisible only by 1
  and itself

  Therefore if any factor is found between 1 and `n`
  `n` is not prime

"""


def isPrime_1(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main():
    for n in range(100):
        print(n, "is a prime:", isPrime_1(n))


main()



####

"""
Complexity
    N == number

    O(N * (N - 1))
    O(N^2 - N)
    => O(N^2)

"""


def isPrime_2(number):
    if number > 1:
        for i in range(1, number):
            for j in range(2, number):
                if i * j == number:
                    return False
    return True


print(isPrime_2(4))
print(isPrime_2(5))

"""
    N == number
    Complexity
        O(N - 1)
        => 𝑂(𝑁)
    prime? == is it divisble by number >= 1 and < number

    Is it divisible by any other number expect 1 and itself
    hence range 2 to number - 1
"""


def isPrime_3(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


print(isPrime_3(4))
print(isPrime_3(5))
