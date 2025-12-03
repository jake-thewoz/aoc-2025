import data_getter

data = data_getter.get_data(3).splitlines()

# print(data)

# Part One

# So we need to find the highest digit, then the highest second digit.

total = 0

for bank in data:
    # find the first digit
    first = ''
    new_bank = ''
    for i in range(9, 0, -1):
        index = bank.find(str(i))
        if index != -1 and index < len(bank)-1:
            first = str(i)
            new_bank = bank[index+1:]
            break

    # now the second digit
    second = ''
    for i in range(9, 0, -1):
        index = new_bank.find(str(i))
        if index != -1:
            second = str(i)
            break

    total += int(first + second)

print(f'The total output joltage is {total}')

# Part Two

# Okay, so I think we take the same approach as above and make it more programmatic

total = 0

for bank in data:
    nbank = bank # strings in python are inherently immutable, so no need to copy

    # this loop will be for our 12 digits
    joltage = ''
    for i in range(11, -1, -1):
        # and in this loop, we'll check for the earliest highest digit
        for j in range(9, 0, -1):
            index = nbank.find(str(j))
            if index != -1 and index < len(nbank)-i:
                joltage = joltage + str(j)
                nbank = nbank[index+1:]
                break
    
    # print(f'final joltage: {joltage}')

    total += int(joltage)

print(f'The new total output joltage is {total}')
