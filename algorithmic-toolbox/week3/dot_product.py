#Uses python3

import sys

def max_dot_product(a, b):
    #if len(a) > 1:
    a.sort()
    b.sort()

    dot_product = [(a_item * b_item) for a_item, b_item in zip(a, b)]
    return sum(dot_product)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
