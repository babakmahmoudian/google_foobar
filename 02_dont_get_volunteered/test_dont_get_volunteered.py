from dont_get_volunteered import solution


def test_given_cast_1():
    src = 0
    dest = 1
    expected = 3

    actual = solution(src, dest)

    assert actual == expected


def test_given_cast_2():
    src = 19
    dest = 36
    expected = 1

    actual = solution(src, dest)

    assert actual == expected
