import data_getter

data = data_getter.get_data(3).splitlines()

# print(data)

# Part One

# So we need to find the highest digit, then the highest second digit.

total = 0

for bank in data:
    print(f'bank: {bank}')
    # find the first digit
    first = ''
    new_bank = ''
    for i in range(9, 0, -1):
        index = bank.find(str(i))
        if index != -1 and index < len(bank)-1:
            first = str(i)
            new_bank = bank[index+1:]
            break

    print(f'first: {first}')
    print(f'new_bank: {new_bank}')

    # now the second digit
    second = ''
    for i in range(9, 0, -1):
        index = new_bank.find(str(i))
        if index != -1:
            second = str(i)
            break

    print(f'second: {second}')
    print(f'and {int(first+second)}')

    total += int(first + second)

print(f'The total output joltage is {total}')


