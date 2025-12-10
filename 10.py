import data_getter

data = data_getter.get_data(10).splitlines()

print(len(data))

[print(row) for row in data]
