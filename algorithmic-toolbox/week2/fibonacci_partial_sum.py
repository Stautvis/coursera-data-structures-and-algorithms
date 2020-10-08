# Uses python3
import sys

def pisano_period(m):
    previous = 0
    current = 1

    for i in range(m*m):
        previous, current = current, (current + previous) % m
        if previous == 0 and current == 1:
            return i + 1

def fibonacci_partial_sum_naive(from_, to):
    period = pisano_period(10)
    return calc_fib(from_ % period, to % period) % 10


def calc_fib(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, (current + next) % 10

    return sum % 10


from_, to = map(int, input().split())
print(fibonacci_partial_sum_naive(from_, to))