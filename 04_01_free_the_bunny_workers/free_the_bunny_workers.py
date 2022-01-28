def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


def combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def solution(num_buns, num_required):
    def add_keys(idx_list, start_index, depth, remaining_keys):
        if depth == num_required - 1:
            key = remaining_keys.pop(-1)
            for i in range(len(dist)):
                if i not in idx_list:
                    dist[i].insert(0, key)
            return

        depth += 1
        for i in range(start_index, len(dist)):
            add_keys(idx_list[:] + [i], i + 1, depth, remaining_keys)

    key_count = combination(num_buns, num_required - 1)

    dist = [[] for i in range(num_buns)]
    add_keys([], 0, 0, range(key_count))

    return dist
