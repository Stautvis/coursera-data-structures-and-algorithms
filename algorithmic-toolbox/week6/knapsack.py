# Uses python3
import sys

def optimal_weight(W, w):
    if 0 in [W, w]: return 0
    result = 0
    
    for x in sorted(w):
        if result + x <= W:
            result += x
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
