#!usr/lib/python3
from random import randint

current = dice_counter = 0

grid = [0, 0, 19, 0, 3, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, -13, 0, -12, 9, -12, 0, 0, 0, 0, 0, -26, 0, 0, 0]

for i in range(0, 10000):
    while True:
        dice = randint(1, 6)
        dice_counter += 1

        if current + dice >= 30:
            break

        current += dice + grid[current + dice - 1]
        
    current = 0

avg = dice_counter / 10000.0

print avg