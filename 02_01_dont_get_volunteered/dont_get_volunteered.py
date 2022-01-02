from Queue import Queue


def solution(src, dest):
    def get_possible_squares(current_square):
        all_moves = []

        if current_square % 8 <= 6:
            all_moves += [-15, 17]

        if current_square % 8 <= 5:
            all_moves += [-6, 10]

        if current_square % 8 >= 2:
            all_moves += [6, -10]

        if current_square % 8 >= 1:
            all_moves += [15, -17]

        all_squares = list(map(
            lambda n: current_square + n, all_moves
        ))

        return [square for square in all_squares if 0 <= square <= 63 and square not in visited]

    explored = Queue(64)
    explored.put(src)

    visited = {src}

    distances = dict.fromkeys(range(64), -1)
    distances[src] = 0

    while not explored.empty():
        current_square = explored.get()
        next_squares = get_possible_squares(current_square)

        if current_square == dest:
            return distances[current_square]

        for square in next_squares:
            visited.add(square)
            explored.put(square)
            distances[square] = distances[current_square] + 1
