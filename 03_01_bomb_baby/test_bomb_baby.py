from bomb_baby import solution


def test_given_case_1():
    m = '2'
    f = '1'
    expected = '1'

    actual = solution(m, f)

    assert actual == expected


def test_given_case_2():
    m = '4'
    f = '7'
    expected = '4'

    actual = solution(m, f)

    assert actual == expected


def test_given_case_impossible():
    m = '2'
    f = '4'
    expected = 'impossible'

    actual = solution(m, f)

    assert actual == expected


def test_possible_large():
    m = str(5 * pow(10, 40) + 123)
    f = str(5 * pow(10, 40) + 124)

    actual = solution(m, f)

    assert actual != 'impossible'


def test_impossible_large():
    m = str(5 * pow(10, 40))
    f = m

    actual = solution(m, f)

    assert actual == 'impossible'


def test_one_one():
    m = '5000'
    f = '1'
    expected = '4999'

    actual = solution(m, f)

    assert actual == expected


def test_both_one():
    m = '1'
    f = '1'
    expected = '0'

    actual = solution(m, f)

    assert actual == expected


def test_same():
    m = '5000'
    f = '5000'
    expected = 'impossible'

    actual = solution(m, f)

    assert actual == expected


def test_multiply():
    m = '50'
    f = '500'
    expected = 'impossible'

    actual = solution(m, f)

    assert actual == expected


def test_big_diff_impossible():
    m = '2'
    f = str(5 * pow(10, 40))
    expected = 'impossible'

    actual = solution(m, f)

    assert actual == expected


def test_big_diff_possible():
    m = '9'
    f = str(5 * pow(10, 40))

    actual = solution(m, f)

    assert actual != 'impossible'
