import data_getter
from collections import deque
import numpy as np

data = data_getter.get_data(9).splitlines()

# print(data)

# Part One

red_tiles = [tuple(int(x) for x in pair.split(',')) for pair in data]

areas = {}

for i in range(len(red_tiles)):
    for j in range(i+1, len(red_tiles)):
        x = sorted((red_tiles[i][0], red_tiles[j][0]), reverse=True)
        y = sorted((red_tiles[i][1], red_tiles[j][1]), reverse=True)

        areas[(i, j)] = (x[0] - x[1] + 1) * (y[0] - y[1] + 1)

print(f'The largest area is {max(areas.values())}')

# Part Two

# I have no idea how to solve this, but...
# I could try making the grid and filling in the green tiles,
# then I could check each area manually?

# What if I skip the grid entirely, and just use sets?

x_max = max(tile[0] for tile in red_tiles)
y_max = max(tile[1] for tile in red_tiles)
x_min = min(tile[0] for tile in red_tiles)
y_min = min(tile[1] for tile in red_tiles)

walls = set()

# Now let's create the borders

for i in range(len(red_tiles)):
    x = red_tiles[i][0]
    y = red_tiles[i][1]

    walls.add((x,y))

    x1 = red_tiles[i-1][0]
    y1 = red_tiles[i-1][1]

    if x1 == x:
        small_y, big_y = sorted([y, y1])
        for j in range(small_y + 1, big_y):
            walls.add((x,j))
    else:
        small_x, big_x = sorted([x, x1])
        for j in range(small_x + 1, big_x):
            walls.add((j,y))

print('done painting #s and Xs')
# Okay... instead of filling the inside, I'll flood the outside with Os

queue = deque([(x_min,y_min)]) # start at the upper left corner, which we know is '.'

directions = [(1,0),(-1,0),(0,1),(0,-1)]

outside = set()

while queue:
    x, y = queue.popleft()

    # fill the space
    outside.add((x,y))

    # Add valid neighbors to the queue
    for dx, dy in directions:
        new_y, new_x = dy + y, dx + x

        # Boundary check
        if y_min-1 <= new_y < y_max+1 and x_min-1 <= new_x < x_max+1:
            # Content check
            if (new_x, new_y) not in outside \
                    and (new_x, new_y) not in walls:
                queue.append((new_x, new_y))

print('done painting Os')
# Now we should have a grid that has the outside filled
# so any valid rectangle will be made up of only #, X, and ., (no Os)

valid_areas = {}
current_max = 0

for i in range(len(red_tiles)):
    for j in range(i+1, len(red_tiles)):

        x = sorted((red_tiles[i][0], red_tiles[j][0]), reverse=True)
        y = sorted((red_tiles[i][1], red_tiles[j][1]), reverse=True)

        if (x[0] - x[1] + 1) * (y[0] - y[1] + 1) < current_max:
            continue

        valid = True
        for k in range(x[1], x[0]+1):
            if (k, y[0]) in outside or (k, y[1]) in outside:
                valid = False
                break
        for k in range(y[1], y[0]+1):
            if (x[0], k) in outside or (x[1], k) in outside:
                valid = False
                break

        if valid:
            current_max = (x[0] - x[1] + 1) * (y[0] - y[1] + 1)
            valid_areas[(i, j)] = (x[0] - x[1] + 1) * (y[0] - y[1] + 1)

print(f'The largest valid area is {current_max}')
