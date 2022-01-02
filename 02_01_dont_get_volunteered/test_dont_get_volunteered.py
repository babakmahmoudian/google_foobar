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


def test_same_source_dest():
    src = 1
    dest = 1
    expected = 0

    actual = solution(src, dest)

    assert actual == expected


def test_going_backwards():
    src = 42
    dest = 25
    expected = 1

    actual = solution(src, dest)

    assert actual == expected


def test_start_to_end():
    src = 0
    dest = 63
    expected = 6

    actual = solution(src, dest)

    assert actual == expected


def test_end_to_start():
    src = 63
    dest = 0
    expected = 6

    actual = solution(src, dest)

    assert actual == expected
