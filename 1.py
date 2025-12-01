import data_getter

data = data_getter.get_data(1).splitlines()

# print(len(data))

# So we start at 50, and go right and left
# If the number ends up at zero, we add one to the count
# Maybe we can do this by just checking %100

safe = 50
count = 0

for move in data:
    if move[0] == 'L':
        safe -= int(move[1:])
    else:
        safe += int(move[1:])

    if safe % 100 == 0:
        count += 1

print(f'The safe hit zero {count} times')

# Part two

# So now we just need to count every time it rolls through zero
# (and every time it lands on zero)

safe = 50
count = 0

# I'm not feeling too smart, so I'm just gonna hard code it

for move in data:
    direction = move[0]
    moves = int(move[1:])

    if direction == 'L':
        for tick in range(moves):
            safe -= 1
            if safe % 100 == 0:
                count += 1

    else:
        for tick in range(moves):
            safe += 1
            if safe % 100 == 0:
                count += 1
                
print(f'The safe rolled through zero {count} times')
