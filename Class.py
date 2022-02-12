#!/usr/bin/env python3


class Calculator:
    def __init__(self, **kwargs):
        self.__operation = kwargs['operation']
        self.__num1 = kwargs['num1']
        self.__num2 = kwargs['num2']

        if self.__operation == 'add':
            print(self.add())
        elif self.__operation == 'subtract':
            print(self.subtract())
        elif self.__operation == 'multiply':
            print(self.multiply())
        elif self.__operation == 'divide':
            print(self.divide())

    def add(self):
        return self.__num1 + self.__num2

    def subtract(self):
        return self.__num1 - self.__num2

    def multiply(self):
        return self.__num1 * self.__num2

    def divide(self):
        return self.__num1 / self.__num2


def main():
    c1 = Calculator(operation='add', num1=10, num2=5)
    c2 = Calculator(operation='subtract', num1=10, num2=5)


if __name__ == '__main__':
    main()
