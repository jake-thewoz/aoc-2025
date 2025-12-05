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

# Let's sort the ranges by the start number, then compare the end number

# First I'll convert them to int tuples
ranges = [
    (int(r.split('-')[0]), int(r.split('-')[1]))
     for r in ranges
    ]

ranges.sort()

# Now we can loop through the ranges, merging if our current
# high number is within the next range

good_ranges = []
skip_list = set()

for i in range(len(ranges)):
    if i in skip_list:
        continue

    low = ranges[i][0]
    high = ranges[i][1]

    for j in range(i+1, len(ranges)):
        if high < ranges[j][0]: # We've found empty space
            break
        elif high >= ranges[j][1]: # The next high number isn't better
            skip_list.add(j)
            continue
        elif high >= ranges[j][0] and high < ranges[j][1]: # The next high number is better
            high = ranges[j][1]
            skip_list.add(j)
            continue

    good_ranges.append((low, high))

# Now I think we have everything we need to calculate the number of IDs

total = 0

for rang in good_ranges:
    total += rang[1] - rang[0] + 1

print(f'The total number of good IDs is {total}')
