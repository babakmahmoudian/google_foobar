from bomb_baby import solution


def test_given_case_1():
    x = '2'
    y = '1'
    expected = 1

    actual = solution(x, y)

    assert actual == expected


def test_given_case_1():
    x = '4'
    y = '7'
    expected = 4

    actual = solution(x, y)

    assert actual == expected


def test_given_case_impossible():
    x = '2'
    y = '4'
    expected = 'impossible'

    actual = solution(x, y)

    assert actual == expected
