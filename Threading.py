#! /usr/bin/env python3

from threading import Thread


class Thread1(Thread):
    def run(self):
        for i in range(10):
            print(f'Hello -> {i}')


class Thread2(Thread):
    def run(self):
        for k in range(10):
            print(f'Hi -> {k}')


def main():
    t1 = Thread1()
    t2 = Thread2()
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
