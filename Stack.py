#! /usr/bin/env python3

class StackTest:

    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def gettop(self):
        return self.items[-1]

    def getstack(self):
        return self.items


def main():
    s1 = StackTest()
    s1.push(1)
    s1.push(2)
    s1.push(3)
    print(s1.getstack())
    s1.pop()
    print(s1.getstack())


if __name__ == '__main__':
    main()
