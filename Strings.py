#! /usr/bin/env python3

a = """My long String"""
print("Length of a:{}".format(len(a)))

b = "There are no free lunches!"
if "free" in b:
    print("Match found")
if "dummy" not in b:
    print("Match not found")

# Slicing
num_of_chars = 5
print(f'{num_of_chars} characters from beginning -> {a[:num_of_chars]}')
print(f'From {num_of_chars}th character till end -> {a[num_of_chars:]}')
print(f'Last {num_of_chars} characters  -> {a[-num_of_chars:]}')
print(f'Last {num_of_chars} characters excluded  -> {a[:-num_of_chars]}')

b = "Hello, World!"
print(b[-5:-2])

# Case change
a = "  Hello, World!  "
print(f'Upper:{a.upper()}  \nLower:{a.lower()} \nWhitespace Removed from before and after string:{a.strip()}')

# Replace
z = "Hello, World!"
print(z.replace("H", "J"))

# Split
k = "Hello,World!"
print(k.split(","))

# format
name = "Rob"
family = "Stark"
age = 19
print("I am {} of {} family. I am {} years of age".format(name, family, age))

#Octal Value
txt = "\110\145\154\154\157"
print("Octal to String -> "+txt)

# Lower vs casfold
a = "I am a Python Programmer"
print(f'Lower -> {a.lower()}  Casefold -> {a.casefold()}')