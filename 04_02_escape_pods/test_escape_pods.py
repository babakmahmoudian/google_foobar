from escape_pods import solution


def test_given_case_1():
    entrances = [0]
    exits = [3]
    path = [[0, 7, 0, 0],
            [0, 0, 6, 0],
            [0, 0, 0, 8],
            [9, 0, 0, 0]]
    expected = 6

    actual = solution(entrances, exits, path)

    assert actual == expected


def test_given_case_2():
    entrances = [0, 1]
    exits = [4, 5]
    path = [[0, 0, 4, 6, 0, 0],
            [0, 0, 5, 2, 0, 0],
            [0, 0, 0, 0, 4, 4],
            [0, 0, 0, 0, 6, 6],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]
    expected = 16

    actual = solution(entrances, exits, path)

    assert actual == expected
