import data_getter

data = data_getter.get_data(9).splitlines()

# print(data)

# Part One

reds = [tuple(int(x) for x in pair.split(',')) for pair in data]

areas = {}

for i in range(len(reds)):
    for j in range(i+1, len(reds)):
        x = sorted((reds[i][0], reds[j][0]), reverse=True)
        y = sorted((reds[i][1], reds[j][1]), reverse=True)

        areas[(i, j)] = (x[0] - x[1] + 1) * (y[0] - y[1] + 1)

print(f'The largest area is {max(areas.values())}')
