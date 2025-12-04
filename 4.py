import data_getter

data = data_getter.get_data(4).splitlines()

# print(f'There are {len(data)} rows with {len(data[0])} columns')

# Part One

count = 0
limit = len(data)

def check_neighbors(y, x):
    rolls = 0

    # The easy ones first (N, S, E, W)
    if y > 0 and data[y-1][x] == '@':
        rolls += 1
    if y < limit-1 and data[y+1][x] == '@':
        rolls += 1
    if x > 0 and data[y][x-1] == '@':
        rolls += 1
    if x < limit-1 and data[y][x+1] == '@':
        rolls += 1

    # now diagnoals
    if y > 0 and x > 0 and data[y-1][x-1] == '@':
        rolls += 1
    if y < limit-1 and x < limit-1 and data[y+1][x+1] == '@':
        rolls += 1
    if x > 0 and y < limit-1 and data[y+1][x-1] == '@':
        rolls += 1
    if x < limit-1 and y > 0 and data[y-1][x+1] == '@':
        rolls += 1

    return rolls

# I'll use ranges rather than iterables on the data, to make coords easier

for y in range(limit):
    for x in range(limit):
        if data[y][x] == '@' and check_neighbors(y, x) < 4:
            count += 1

print(f'There were {count} rolls accessible')

# Part Two

# Now we just need to loop and replace until there are no replacements

# First I'll make a copy of the data so we can safely mutate it
grid = [list(row) for row in data]
