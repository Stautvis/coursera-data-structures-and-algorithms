#Uses python3

import sys

def lcs2(a, b):
    n = len(a) 
    m = len(b) 
  
    table = [[0] * (m + 1)] * (n + 1)

    for ni in range(1, n+1): 
        for mi in range(1, m+1): 
            if a[ni-1] == b[mi-1]: 
                table[ni][mi] = table[ni-1][mi-1]+1
            else: 
                table[ni][mi] = max(
                    table[ni-1][mi],
                    table[ni][mi-1]
                ) 
                
    return table[n][m]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
