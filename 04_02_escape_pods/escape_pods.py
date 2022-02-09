def solution(entrances, exits, path):
    v = len(path)
    source_row = [0 for i in range(v)]
    terminal_row = [0 for i in range(v)]
    path.extend([source_row, terminal_row])
    for row in path:
        row.extend([0, 0])
    for i in entrances:
        source_row[i] = float('inf')
    for i in exits:
        path[i][v + 1] = float('inf')
    return edmonds_karp(path, v, v + 1)


def edmonds_karp(graph, source, sink):

    total_flow = 0

    while True:

        predecessors = bfs_traverse(graph, source)

        if predecessors[sink] is None:
            break

        flow = float('inf')

        node = sink
        while node != source:
            flow = min(flow, graph[predecessors[node]][node])
            node = predecessors[node]

        node = sink
        while node != source:
            graph[predecessors[node]][node] -= flow
            graph[node][predecessors[node]] += flow
            node = predecessors[node]

        total_flow += flow

    return total_flow


def bfs_traverse(graph, source):

    queue = [source]
    predecessors = [None] * len(graph)

    while queue:
        current_node = queue.pop()
        for node, flow in enumerate(graph[current_node]):
            if predecessors[node] is not None:
                continue
            if flow == 0:
                continue
            predecessors[node] = current_node
            queue.append(node)

    return predecessors
