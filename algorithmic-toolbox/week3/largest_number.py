#Uses python3

import sys
from functools import cmp_to_key

def largest_number(a):
    a.sort(key=cmp_to_key(is_greater))
    return "".join([str(i) for i in a])

def is_greater(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    return int(ba) - int(ab)       
    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
