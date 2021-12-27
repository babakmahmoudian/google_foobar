from solar_doomsday import solution


def test_finds_distinct_squares():
    area = 15324
    expected = [15129, 169, 25, 1]

    actual = solution(area)

    assert actual == expected


def test_finds_recurring_squares():
    area = 12
    expected = [9, 1, 1, 1]

    actual = solution(area)

    assert actual == expected
