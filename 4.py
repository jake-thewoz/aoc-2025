import data_getter

data = data_getter.get_data(4).splitlines()

# print(f'There are {len(data)} rows with {len(data[0])} columns')

# Part One

count = 0
LIMIT = len(data)

def check_neighbors(y, x, grid):
    rolls = 0

    # The easy ones first (N, S, E, W)
    if y > 0 and grid[y-1][x] == '@':
        rolls += 1
    if y < LIMIT-1 and grid[y+1][x] == '@':
        rolls += 1
    if x > 0 and grid[y][x-1] == '@':
        rolls += 1
    if x < LIMIT-1 and grid[y][x+1] == '@':
        rolls += 1

    # now diagnoals
    if y > 0 and x > 0 and grid[y-1][x-1] == '@':
        rolls += 1
    if y < LIMIT-1 and x < LIMIT-1 and grid[y+1][x+1] == '@':
        rolls += 1
    if x > 0 and y < LIMIT-1 and grid[y+1][x-1] == '@':
        rolls += 1
    if x < LIMIT-1 and y > 0 and grid[y-1][x+1] == '@':
        rolls += 1

    return rolls

# I'll use ranges rather than iterables on the data, to make coords easier

for y in range(LIMIT):
    for x in range(LIMIT):
        if data[y][x] == '@' and check_neighbors(y, x, data) < 4:
            count += 1

print(f'There were {count} rolls accessible')

# Part Two

# Now we just need to loop and replace until there are no replacements

# First I'll make a copy of the data so we can safely mutate it
diagram = [list(row) for row in data]

count = 0
removes = 1

while removes != 0:
    removes = 0

    for y in range(LIMIT):
        for x in range(LIMIT):
            if diagram[y][x] == '@' and check_neighbors(y, x, diagram) < 4:
                count += 1
                removes += 1
                diagram[y][x] = '.'

print(f'We removed {count} total rolls')
