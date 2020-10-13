#Uses python3

import sys

def lcs3(a, b, c):
    n = len(a)
    m = len(b)
    l = len(c)

    if 0 in [n, m, l]: return 0 #if any sequence has no elements, then there isn't common subsequence
    lcs = [[[0] * (l + 1)] * (m + 1)] * (n + 1)

    for ni in range(1,n + 1):
        for mi in range(1,m + 1):
            for li in range(1, l + 1):
                if a[ni - 1] == b[mi - 1] and a[ni - 1] == c[li - 1]:
                    lcs[ni][mi][li] = lcs[ni - 1][mi - 1][li - 1] + 1
                else:
                    lcs[ni][mi][li] =   max(max(lcs[ni - 1][mi][li],
                                            lcs[ni][mi - 1][li]),
                                            lcs[ni][mi][li -1])
    return lcs[n][m][l]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
