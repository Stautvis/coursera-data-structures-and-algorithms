# Uses python3
import sys
import random

def partition3(a, l, r):
    item, pivot = l, a[l]

    while item <= r:     
        if a[item] < pivot:
            a[l], a[item] = a[item], a[l]
            l += 1
            item += 1
        elif a[item] > pivot:
            a[item], a[r] = a[r], a[item]
            r -= 1
        else:
            item += 1
            
    return l, r

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2= partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
