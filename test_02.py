import advent02


def test_examples():
    """+1, -1 first reaches 0 twice.
+3, +3, +4, -2, -4 first reaches 10 twice.
-6, +3, +8, +5, -6 first reaches 5 twice.
+7, +7, -2, -7, -4 first reaches 14 twice.
"""
    assert advent02.solve([1, -1]) == 0
    assert advent02.solve([3, 3, 4, -2, -4]) == 10
    assert advent02.solve([-6, 3, 8, 5, -6]) == 5
    assert advent02.solve([7, 7, -2, -7, -4]) == 14

