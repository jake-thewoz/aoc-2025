import data_getter
from collections import deque

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

# New approach!
# Let's 'compress' the grid down, look for the biggest area,
# then look up the true area with the original tiles.

# First, let's compress
unique_numbers = set()
for x, y in red_tiles:
    unique_numbers.add(x)
    unique_numbers.add(y)

sorted_unique = sorted(list(unique_numbers))

# Now we'll create a sort of compression map, where we map the 
# original values to the 'compressed' indexes

compression_map = {
    original: index
    for index, original in enumerate(sorted_unique)
}

# Now we can create a compressed version of the original tiles!

c_tiles = []
for x, y in red_tiles:
    c_x = compression_map[x]
    c_y = compression_map[y]

    c_tiles.append((c_x, c_y))

# Now that we have a compressed set of tiles, we can create a grid without
# breaking the computer

grid = [['.' for _ in range(len(unique_numbers)+1)] for _ in range(len(unique_numbers)+1)]


