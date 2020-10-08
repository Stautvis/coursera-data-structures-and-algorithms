# Uses python3
import sys

def get_change(m):
    denominations = [10, 5, 1]
    current_denomination_index = 0
    count = 0

    while(m > 0):
        current_denomination = denominations[current_denomination_index]
        if(denominations[current_denomination_index] > m):
            current_denomination_index += 1
            continue
        times = fit_inside(m, current_denomination)
        m -= times * current_denomination
        count += times
    return count

def fit_inside(m,n):
    return int(m/n)


m = int(input())
print(get_change(m))
