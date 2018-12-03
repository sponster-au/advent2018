import sys
import itertools as it


def parse(s):
    return [int(line) for line in s.splitlines()]


def solve(data):
    freq = 0
    seen = set([freq])
    for n in it.cycle(data):
        freq += n
        if freq in seen:
            return freq
        seen.add(freq)


if __name__ == '__main__':
    data = open(sys.argv[1]).read()
    data = parse(data)
    print(solve(data))
