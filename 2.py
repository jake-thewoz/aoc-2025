import data_getter

data = data_getter.get_data(2).split(',')

# print(data)

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

# Part two

# I feel like there's a way to do this with DP, but I can't figure it out, lol
# Let's just make a function and manually test

def is_invalid(number):
    snumber = str(number)

    # Let's try to eliminate some by seeing if the back half of the number
    #  uses different chars than the front half
    mid = len(snumber) // 2
    if set(snumber[mid:]) != set(snumber[:mid]):
        return False

    # If we made it this far, lets get to loopin
    # We'll loop through 1 to len//2
    for i in range(1, mid+1):
        # Let's move on if i doesn't equally divide into the length
        if len(snumber) % i != 0:
            continue
        
        # Now we'll grab the pattern to check for, and loop through the other sections
        pattern = snumber[:i]
        pattern_works = True
        for k in range(1, (len(snumber)//i)):
            start = k*i
            end = (k+1)*i
            if pattern != snumber[start:end]:
                pattern_works = False
                break

        if pattern_works:
            return True

    return False

# Now let's restart our variable and loop through the data

invalid_id_sum = 0

for id_range in data:
    first = id_range.split('-')[0]
    last = id_range.split('-')[1]

    for number in range(int(first), int(last)+1):
        if is_invalid(number):
            invalid_id_sum += number

print(f'The sum of all invalid ids for part two is {invalid_id_sum}')
