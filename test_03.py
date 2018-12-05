import advent03


def test_examples():
    s = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""
    d = advent03.parse(s)
    assert advent03.solve(d) == 4

    assert advent03.solve2(d) == 3

