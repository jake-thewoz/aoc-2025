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

# Part Two

# This doesn't seem that bad-
# All we need to do is modify our function so that we create paths instead of
# just count.

# Well this is taking a long time to run. I'm not sure why, but my guess is:
# - there are cycles
# - there are a ton of routes
# I think cycles is a more likely culprit...

def find_routes(graph, start_node, end_node, path=[]):
    # Update the current path
    current_path = path + [start_node]

    if start_node == end_node:
        return [current_path]

    # Recursive section
    all_paths = []

    # iterate through all neighbors
    for neighbor in graph[start_node]:
        # collect their paths to end_node
        new_paths = find_routes(graph, neighbor, end_node, current_path)

        # add the new paths to all paths
        all_paths.extend(new_paths)

    return all_paths

# print(f'The number of ways to get from svr to end is {count_routes(graph, "svr", "out")}')

all_paths = find_routes(graph, 'svr', 'out')
filtered_paths = [path for path in all_paths if 'dac' in path and 'fft' in path]

print(f'The number of paths with dac and fft are {len(filtered_paths)}')
