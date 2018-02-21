import time

largest_number = None
for num in [9, 45, 47, 48, 97, 102]:
    if largest_number is None:
        largest_number = num
    elif num > largest_number:
        largest_number = num

print(largest_number)

tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)

zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)
