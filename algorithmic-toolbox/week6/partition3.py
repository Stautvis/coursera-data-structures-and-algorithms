# Uses python3
import sys
import itertools

def partition3(A):
    sum_of_elements = sum (A)
    if sum_of_elements % 3 != 0: return 0
    
    count = 0 
    value = [[0 for i in range(W + 1)] for i in range(n + 1)]

    for i in range(1, W+1):
        for j in range(1, n+1):
            value[i][j] = value[i][j-1]
            if items[j-1] <= i:
                temp = value[i - items[j - 1]][j - 1] + items[j - 1]
            if temp > value[i][j]:
                value[i][j] = temp
            if value[i][j] == W: count += 1
    return 1    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

