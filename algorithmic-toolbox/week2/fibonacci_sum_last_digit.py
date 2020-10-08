# Uses python3
import sys

def pisano_period(m):
    previous = 0
    current = 1

    for i in range(m*m):
        previous, current = current, (current + previous) % m
        if previous == 0 and current == 1:
            return i + 1

def calc_fib(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1
    
    for i in range(n - 1):
        previous, current = current, (previous + current) % 10
        sum += current
    return  sum

def fibonacci_sum_naive(n):
    return calc_fib(n % pisano_period(10)) % 10



n = int(input())
print(fibonacci_sum_naive(n))
