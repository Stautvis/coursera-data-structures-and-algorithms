#Uses python3

import sys

def lcs2(a, b):
    n = len(a) 
    m = len(b) 
  
    # declaring the array for storing the dp values 
    counter = [[None]*(m+1) for i in range(n+1)] 

    for i in range(n+1): 
        for j in range(m+1): 
            if i == 0 or j == 0 : 
                counter[i][j] = 0
            elif a[i-1] == b[j-1]: 
                counter[i][j] = counter[i-1][j-1]+1
            else: 
                counter[i][j] = max(counter[i-1][j] , counter[i][j-1]) 
                
    return counter[m][n]

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
