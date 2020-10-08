# Uses python3
import sys

def get_majority_element(a, left, right):
    if len(a) <= 1:
        return -1
    frequency = {i:a.count(i) for i in a}
    majority = max(frequency.values())
    return 1 if len(a)/2 < majority else -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
