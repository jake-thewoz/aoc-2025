import data_getter

data = data_getter.get_data(6).splitlines()

# print(data)

# Part One

# Let's get our data into a list of tuples

homework = [tuple(row.split()) for row in data]

# Next we'll go through each column and add or multiply them all

add = False
total = 0

for i in range(len(homework[0])):
    column = 0

    if homework[4][i] == '+':
        add = True
    else: # multiplication needs to start at one
        add = False
        column = 1


    for j in range(4):
        if add:
            column += int(homework[j][i])
        else:
            column *= int(homework[j][i])

    total += column

print(f'The grand total is {total}')
