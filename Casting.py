#!/usr/bin/env python3

# float to int
# string to int
a = 1
b = int(1)
c = int(1.2)
d = int("1")

if a == b & a == c & a == d:
    print("All variables are equal")

# int to str
# float to str
a = "1"
d = "1.2"
b = str(1)
c = str(1.2)

if a == b:
    print("int to string casting is successful")
if d == c:
    print("float to string casting is successful")

