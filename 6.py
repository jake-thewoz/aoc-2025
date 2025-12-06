import data_getter
import math

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

# Part Two

# Wow, kind of tricky.
# I think we can loop through every character in one row,
# collecting the numbers and combining when we find the operator.

homework = data[:]
numbers = []
total = 0

# Our main loop will go backwards through every character in a row
for i in range(len(homework[0])-1, -1, -1):
    number = ''

    # Here we go down the columns for each row-character
    for j in range(len(homework)-1):
        number += homework[j][i]

    # And if it's not a blank space, we add the number to our list
    if number.strip() != '':
        numbers.append(int(number))

    # If the final row has an operator, we add or mult them up
    if homework[4][i] != ' ':
        # Go time!
        if homework[4][i] == '+':
            total += sum(numbers)
        else:
            total += math.prod(numbers)

        # Now we reset numbers
        numbers = []

print(f'The new grand total is {total}')
