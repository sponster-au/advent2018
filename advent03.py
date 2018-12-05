import sys
import re
from pprint import pprint


pattern = re.compile("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")

def parse(s):
    """ parse into {id: (x0, y0, x1, y1)}
    """
    d = {}
    for line in s.splitlines():
        match = pattern.match(line)
        id_s, x0_s, y0_s, w_s, h_s = match.groups()
        _id = int(id_s)
        x0 = int(x0_s)
        y0 = int(y0_s)
        x1 = x0 + int(w_s) - 1 
        y1 = y0 + int(h_s) - 1
        d[_id] = (x0, y0, x1, y1)
    # pprint(d)
    return d

    return [int(line) for line in s.splitlines()]


def dump(grid):
    for row in grid:
        print(row)
    print()


def solve(data):
    pprint(data)
    X = max(v[2] for v in data.values())
    Y = max(v[3] for v in data.values())
    grid = [[0 for x in range(X + 1)] for y in range(Y + 1)]
    dump(grid)
    for k in sorted(data.keys()):
        (x0, y0, x1, y1) = data[k]
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                grid[y][x] += 1
        dump(grid)
    overlaps = 0
    for row in grid:
        for c in row:
            if c > 1:
                overlaps += 1
    return overlaps


if __name__ == '__main__':
    data = open(sys.argv[1]).read()
    data = parse(data)
    print(solve(data))
