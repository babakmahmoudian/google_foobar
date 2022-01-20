from prepare_the_bunnies_escape import solution


def test_given_case_1():
    map = [[0, 1, 1, 0],
           [0, 0, 0, 1],
           [1, 1, 0, 0],
           [1, 1, 1, 0]]
    expected = 7

    actual = solution(map)

    assert actual == expected


def test_given_case_2():
    map = [[0, 0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 1, 1, 1, 1, 1],
           [0, 1, 1, 1, 1, 1],
           [0, 0, 0, 0, 0, 0]]
    expected = 11

    actual = solution(map)

    assert actual == expected
