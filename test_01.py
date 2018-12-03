import advent01


def test_examples():
    """+1, +1, +1 results in  3
+1, +1, -2 results in  0
-1, -2, -3 results in -6
"""
    assert advent01.solve([1, 1, 1]) == 3
    assert advent01.solve([1, 1, -2]) == 0
    assert advent01.solve([-1, -2, -3]) == -6

