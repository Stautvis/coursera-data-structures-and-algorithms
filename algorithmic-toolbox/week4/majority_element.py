# Uses python3
import sys

def get_majority_element(a, left, right):
    count = {}
    n = len(a)

    for i in a:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
        if count[i] > n/2:
            return 1
    return -1
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
