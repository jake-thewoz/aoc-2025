import data_getter

data = data_getter.get_data(2).split(',')

print(data)

# There are a couple ways to go about this...
# - we could make ranges, then test inclusion based on all the known repeats
# - we could loop through the ranges, and manually test for repeats

# Because I'm short on time, I'll do the latter

invalid_id_sum = 0

for id_range in data:
    first = id_range.split('-')[0]
    last = id_range.split('-')[1]

    for number in range(int(first), int(last)+1):
        # first we'll rule out any ids with odd numbers of digits
        if len(str(number)) % 2 == 1:
            continue

        # then we'll divide in half and compare
        middle = len(str(number)) // 2
        first_half = str(number)[:middle]
        second_half = str(number)[middle:]

        if first_half == second_half:
            invalid_id_sum += number

print(f'The sum of all invalid ids is {invalid_id_sum}')

