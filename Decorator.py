#!/usr/bin/env python3

import time


def elapsed_time(f):
    def calculate_time(terms):
        t1 = time.time()
        f(terms)
        t2 = time.time()
        print(f'Time taken by function -> {t2 - t1}')
    return calculate_time


@elapsed_time
def fibonacci(terms):
    n1, n2 = 0, 1
    count = 0
    while count < terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


def main():
    fibonacci(7)


if __name__ == '__main__':
    main()
