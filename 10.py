import data_getter
import itertools
from collections import deque

data = data_getter.get_data(100).splitlines()

# print(data)

# Part One

# I found a reddit comment explaining how this can be done with BFS:
# https://www.reddit.com/r/adventofcode/comments/1pivxwg/comment/nt99fg4/

# First let's wrangle the data into a dict
# This is so ugly, but it gets our data into a dict where the key is a tuple
# of the light state, and the value is a list of lists of ints (the presses)
machines = {
    tuple(list(row.split(' ')[0])[1:-1]): 
    [
        [int(s) for s in item.strip('()').split(',')]
        for item in row.split(' ')[1:-1]
    ]
    for row in data
}

# print(machines)

# I'll try to implement this BFS approach
# Essentially, the state of the lights are the nodes, and the button presses
# are paths that connect nodes. 

def button_bfs(target_state, press_list):
    # first we'll convert the states into tuples of booleans
    start_state = (False,) * len(target_state)
    target_state = tuple(char == '#' for char in target_state)

    # print(start_state)
    # print(target_state)

    if start_state == target_state:
        return 0

    queue = deque([(start_state, 0)])
    visited = {start_state}

    # main search loop
    while queue:
        # dequeue the current node and its distance
        current_node, distance = queue.popleft()

        # Let's create the next level of the graph
        graph = []
        for press in press_list:
            # print(current_node)
            # print(press)
            new_node = [
                (not value) if index in press else value
                for index, value in enumerate(current_node)
            ]
            # print(new_node)
            graph.append(tuple(new_node))

        # now let's explore these new nodes
        for neighbor in graph:

            # success condition
            if neighbor == target_state:
                # print(f'Success: {distance+1}')
                return distance + 1

            # continue if neighbor hasn't been visited
            if neighbor not in visited:
                visited.add(neighbor)
                # add it to the queue
                queue.append((neighbor, distance+1))
    return -1

# Now let's run it!
count = 0
for state, presses in machines.items():
    count += button_bfs(state, presses)

print(count)

# That didn't work.
# Let's try something simpler:
# - we know that each button at most can only be pressed once
# - so some combination of the buttons must equal the lights

def button_combo(target_state, press_list):
    start_state = (False,) * len(target_state)
    target_state = tuple(char == '#' for char in target_state)

    # Let's go from 1 to len(state), trying every combination of buttons
    for r in range(1, len(target_state)+1):
        combos = list(itertools.combinations(press_list, r))
        
        # Each combo is a list of the button presses
        for combo in combos:

            new_state = list(start_state)
            for press in combo:
                new_state = [
                    (not value) if index in press else value
                    for index, value in enumerate(new_state)
                ]
                if tuple(new_state) == target_state:
                    return r
    return 0

# Let's try again!
count = 0
for state, presses in machines.items():
    count += button_combo(state, presses)

print(count)
