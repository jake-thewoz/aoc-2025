import data_getter
import math

data = data_getter.get_data(8).splitlines()

# print(data)

# Part One

boxes = [tuple(int(num) for num in box.split(',')) for box in data]

def find_euclidean(p, q):
    p1, p2, p3 = boxes[p]
    q1, q2, q3 = boxes[q]

    return math.sqrt((p1 - q1)**2 + (p2 - q2)**2 + (p3 - q3)**2)

# This will keep indexes and their distances
distances = {}

# Now we'll loop through all connections and add them to distances
for i in range(len(boxes)):
    for k in range(len(boxes)):
        small, big = sorted([i, k])
        if small == big:
            continue
        elif (small, big) in distances:
            continue
        else:
            distances[(small, big)] = find_euclidean(small, big)

# Now we get them in order, so the shortest distnaces are first
sorted_distances = sorted(distances.items(), key=lambda item: item[1])

shortest_thousand = [item[0] for item in sorted_distances[:1000]]

# Now we're going to use the Union-Find algorithm
# https://en.wikipedia.org/wiki/Disjoint-set_data_structure

def find_circuits(pairs):
    # 1. Gather all unique boxes (nodes)
    unique_nodes = set()
    for u, v in pairs:
        unique_nodes.add(u)
        unique_nodes.add(v)

    # The 'parent' dictionary maps a node to its parent in the set.
    # Initially, every node is its own parent (a set of size 1).
    parent = {node: node for node in unique_nodes}

    def find_set(node):
        """Finds the representative (root) of the set containing 'node'."""
        if parent[node] == node:
            return node
        # Path compression for efficiency: set the node's parent directly to the root
        parent[node] = find_set(parent[node])
        return parent[node]

    def union_sets(node1, node2):
        """Unites the sets containing node1 and node2."""
        root1 = find_set(node1)
        root2 = find_set(node2)
        if root1 != root2:
            # Union by rank/size (here, simply setting root1's parent to root2)
            parent[root1] = root2
            return True # Successfully merged a component
        return False # Already in the same component

    # 2. Process all pairs to build the connections
    for u, v in pairs:
        union_sets(u, v)

    # 3. Group the original pairs by their connected component root
    # The 'root' of a pair (u, v) is the root of its first element, u.
    components_map = {}
    for u, v in pairs:
        root = find_set(u)
        if root not in components_map:
            components_map[root] = []
        components_map[root].append((u, v))

    # The values of the dictionary are the final connected components
    return list(components_map.values())

circuits = find_circuits(shortest_thousand)
print(circuits)

# Now we need to find the 3 largest circuits
circuit_sizes = [len(circuit) for circuit in circuits]
three_biggest = sorted(circuit_sizes, reverse=True)[:3]

print(f'The three biggest circuits make a product of {math.prod(three_biggest)}')
