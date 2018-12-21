import sys
import string


def parse(s):
    return s.strip()


def solve(data):
    while data:
        changed = False
        for c in string.ascii_lowercase:
            C = c.upper()
            cC = c + C
            Cc = C + c
            data2 = data.replace(cC, "").replace(Cc, "")
            if data2 != data:
                data = data2
                changed = True
        if not changed:
            break
    return data


def solve2(data):
    X = []
    for c in sorted(set(d.lower() for d in data)):
        C = c.upper()
        dd = data.replace(c, "").replace(C, "")
        x = solve(dd)
        # print(c, data, dd, x)
        X.append(x)
    X = sorted(X, key=len)
    return X[0]


if __name__ == '__main__':
    data = open(sys.argv[1]).read()
    data = parse(data)
    print(len(solve(data)))
    print(len(solve2(data)))
