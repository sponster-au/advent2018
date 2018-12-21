import advent05


def test_examples():
    s = "dabAcCaCBAcCcaDA"
    d = advent05.parse(s)
    assert advent05.solve(d) == "dabCBAcaDA"


def test_examples2():
    s = "dabAcCaCBAcCcaDA"
    d = advent05.parse(s)
    assert advent05.solve2(d) == "daDA"

