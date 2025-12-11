import data_getter

data = data_getter.get_data(11).splitlines()

# print(data)

# Part One

# I think we can use a recursive function to find all the routes
# hopefully, without breaking the computer

# First let's turn this data into a dict
graph = {row.split(':')[0]: tuple(row.split(' ')[1:]) for row in data}

# Here's our recursive route counter
# Hopefully there are no cycles....
def count_routes(graph, start_node, end_node):
    if start_node == end_node:
        return 1

    count = 0
    
    # iterate through all connections of the current node
    for neighbor in graph[start_node]:
        # count up their paths to the end node
        count += count_routes(graph, neighbor, end_node)

    return count

print(f'The number of ways to get from you to end is {count_routes(graph, "you", "out")}')
