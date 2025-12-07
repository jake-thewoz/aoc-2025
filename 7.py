import data_getter

data = data_getter.get_data(7).splitlines()

# print(data)

# Part One

diagram = [list(row) for row in data]
start = diagram[0].index('S')
diagram[1][start] = '|'

# I think I can do this with a simple loop
# We just have to look ahead one row

count = 0

for i in range(1, len(diagram)-1):
    for j in range(len(diagram[0])):
        if diagram[i][j] == '|':
            if diagram[i+1][j] == '^':
                count += 1
                diagram[i+1][j-1] = '|'
                diagram[i+1][j+1] = '|'
            elif diagram[i+1][j] == '.':
                diagram[i+1][j] = '|'

print(f'The total number of splits is {count}')

# Part Two

# This was so tricky, had to use a visualization on reddit
# https://www.reddit.com/r/adventofcode/comments/1pgbg8a/

# The idea is that each beam, or each x value in the graph,
# has a finite number of unique paths to get there.

# You can add them up as you traverse down, then add every value
# together at the end to find the total number of unique paths.

x = [0] * len(diagram[0])
x[start] = 1

for i in range(1, len(diagram)-1):
    for j in range(len(diagram[0])):
        if diagram[i+1][j] == '^':
            x[j-1] += x[j]
            x[j+1] += x[j]
            x[j] = 0

print(f'The total number of timelines is {sum(x)}')
