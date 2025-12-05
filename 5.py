import data_getter

data = data_getter.get_data(5).splitlines()

# print(data)

blank = data.index('')

ranges = data[:blank]
ingredients = data[blank+1:]

# Part One

# I think we can go through each id and check if it's in one of the ranges
# No need for anything crazy yet

count = 0

for ing in ingredients:
    for rang in ranges:
        low, high = rang.split('-')
        if int(ing) >= int(low) and int(ing) <= int(high):
            count += 1
            break

print(f'There were {count} fresh ingredients')

# Part Two

# Okay, we'll just subtract and add one

# Ah, it's not that simple! They overlap!
# Let's see if our computer breaks if we try to put them all in a set

# Update, it did break, lol. Process killed
# Let's try making a more perfect list of ranges, combining the ones that overlap, then count
# Maybe we need to do it multiple times?

kill_list = {1}
old_ranges = ranges[:]

while len(kill_list) > 0:
    kill_list = set()
    new_ranges = []

    for i in range(len(old_ranges)):
        if i in kill_list:
            continue

        low, high = [int(x) for x in old_ranges[i].split('-')]

        for j in range(i+1, len(old_ranges)):
            if j in kill_list:
                continue

            jlow, jhigh = [int(x) for x in old_ranges[j].split('-')]
            
            if low >= jlow and low <= jhigh:
                low = jlow
                kill_list.add(j)
            if high >= jlow and high <= jhigh:
                high = jhigh
                kill_list.add(j)

        new_ranges.append(f'{low}-{high}')
    old_ranges = new_ranges[:]

# Now we just add up the differences

total = 0

for rang in new_ranges:
    low, high = [int(x) for x in rang.split('-')]
    total += high - low + 1

print(f'The total number of fresh IDs is {total}')
