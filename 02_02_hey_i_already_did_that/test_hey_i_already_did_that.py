from hey_i_already_did_that import solution


def test_given_cast_1():
    n = '210022'
    b = 3
    expected = 3

    actual = solution(n, b)

    assert actual == expected


def test_given_cast_2():
    n = '1211'
    b = 10
    expected = 1

    actual = solution(n, b)

    assert actual == expected
