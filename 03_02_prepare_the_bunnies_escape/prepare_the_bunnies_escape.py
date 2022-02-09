from queue import Queue


def get_neighbors(map, node):
    neighbors = []

    row = node[0]
    col = node[1]
    maxrow = len(map) - 1
    maxcol = len(map[0]) - 1

    if row < maxrow and map[row + 1][col] == 0:
        neighbors.append((row + 1, col))
    if row > 0 and map[row - 1][col] == 0:
        neighbors.append((row - 1, col))
    if col < maxcol and map[row][col + 1] == 0:
        neighbors.append((row, col + 1))
    if col > 0 and map[row][col - 1] == 0:
        neighbors.append((row, col - 1))

    return neighbors


def bfs(map):
    src = (0, 0)
    dest = (len(map) - 1, len(map[0]) - 1)
    no_path_len = len(map) * len(map[0])

    explored = Queue(64)
    explored.put(src)

    visited = {src}

    distances = dict.fromkeys([(i, j) for j in range(len(map[0])) for i in range(len(map))], -1)
    distances[src] = 0

    while not explored.empty():
        current_node = explored.get()
        next_nodes = get_neighbors(map, current_node)

        if current_node == dest:
            return distances[dest] + 1

        for node in next_nodes:
            if node in visited:
                continue
            visited.add(node)
            explored.put(node)
            distances[node] = distances[current_node] + 1

    return no_path_len


def solution(map):
    shortest_len = bfs(map)

    if shortest_len == len(map) + len(map[0]) - 1:
        return shortest_len

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                continue

            if len(get_neighbors(map, (i, j))) < 2:
                continue

            map[i][j] = 0
            new_path_len = bfs(map)
            shortest_len = min(shortest_len, new_path_len)
            map[i][j] = 1

    return shortest_len
