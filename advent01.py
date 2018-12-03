import sys


def parse(s):
    return [int(line) for line in s.splitlines()]


def solve(data):
    return sum(data)


if __name__ == '__main__':
    data = open(sys.argv[1]).read()
    data = parse(data)
    print(solve(data))