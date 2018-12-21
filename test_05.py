import advent05


def test_examples():
    s = "dabAcCaCBAcCcaDA"
    d = advent05.parse(s)
    assert advent05.solve(d) == "dabCBAcaDA"

