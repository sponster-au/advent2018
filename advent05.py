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


if __name__ == '__main__':
    data = open(sys.argv[1]).read()
    data = parse(data)
    print(solve(data))
