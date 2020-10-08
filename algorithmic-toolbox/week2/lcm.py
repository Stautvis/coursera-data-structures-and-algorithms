# Uses python3
import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm_naive(a, b):
    return int(a * b / gcd(a, b))


a, b = map(int, input().split())
print(lcm_naive(a, b))

