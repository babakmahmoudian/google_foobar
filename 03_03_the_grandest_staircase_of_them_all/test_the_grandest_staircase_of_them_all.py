from the_grandest_staircase_of_them_all import solution


def test_given_case_1():
    n = 200
    expected = 487067745

    actual = solution(n)

    assert actual == expected


def test_given_case_2():
    n = 3
    expected = 1

    actual = solution(n)

    assert actual == expected
