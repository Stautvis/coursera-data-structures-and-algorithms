# Uses python3
import sys
import math
from typing import SupportsAbs

def optimal_summands(n):
    summands = []
    k=int((math.sqrt(1+(8*n))-1)/2)
    diff=int(n-((k-1)*k/2))

    for i in range(k - 1):
        summands.append(i+1);
    summands.append(diff)

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
