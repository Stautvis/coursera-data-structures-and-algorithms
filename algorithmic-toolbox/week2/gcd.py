# Uses python3
import sys

def gcd_naive(a, b):
    if b == 0:
        return a
    return gcd_naive(b, a % b)


a, b = map(int, input().split())
print(gcd_naive(a, b))
