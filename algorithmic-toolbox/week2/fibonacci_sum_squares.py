# Uses python3
from sys import stdin

def pisano_period(m):
    previous = 0
    current = 1

    for i in range(m*m):
        previous, current = current, (current + previous) % m
        if previous == 0 and current == 1:
            return i + 1

def calc_fib(n):
    sum = 0
    previous = 0
    current  = 1
    
    for i in range(n + 1):
        sum += (previous * previous) % 10
        previous, current = current, (previous + current) % 10

    return  sum % 10

def fibonacci_sum_squares_naive(n):
    return calc_fib(n % pisano_period(10))

n = int(input())
print(fibonacci_sum_squares_naive(n))
