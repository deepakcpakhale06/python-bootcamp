#! /usr/bin/env python3

# while loop - break and continue
start = 1
end = 100
while start <= end:

    if start == 100 / 2:
        print("!!!Skipping!!!")
        start += 1
        continue
    elif start == end:
        print(f'Counter is on {end} and loop is exiting now')
        break
    else:
        print(f'Current value: {start}')
    start += 1

print("================================")

# for loop-List
num_list = [0, 90, 20, 40]
for num in num_list:
    print(f'Lucky number is {num}')

# for loop-String
for c in "aeroplane":
    print(c)

# Find favorite animal
my_fav_animal = "tiger"
animal_list = ["elephant", "lion", "duck", "tiger"]
for animal in animal_list:
    if animal == my_fav_animal:
        print(f'Found favorite animal {animal}')
        break
