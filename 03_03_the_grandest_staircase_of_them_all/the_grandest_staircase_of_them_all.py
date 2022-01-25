def solution(n):
    def get_staircases(remained_bricks_count, previous_height, memo):
        if (remained_bricks_count, previous_height) in memo:
            return memo[(remained_bricks_count, previous_height)]
        if remained_bricks_count == 0:
            return 1
        if remained_bricks_count < 0:
            return 0

        staircase_count = 0
        for stair_height in range(1, previous_height):
            count = get_staircases(
                remained_bricks_count - stair_height,
                stair_height,
                memo
            )
            staircase_count += count

        memo[(remained_bricks_count, previous_height)] = staircase_count
        return staircase_count

    return get_staircases(n, n, {})
