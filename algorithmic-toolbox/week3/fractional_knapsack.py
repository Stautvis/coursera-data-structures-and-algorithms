# Uses python3
import sys


def fit_inside(m,n):
    return int(m/n)

def get_optimal_value(capacity, weights, values):
    value = 0
    per_units = [(value / weight) for value, weight in zip(values, weights)]

    while(capacity > 0):
        if(len(per_units) == 0):
            break

        max_index = per_units.index(max(per_units))
        

        if(capacity >= weights[max_index]):
            capacity -= weights[max_index]
            value += values[max_index]

            weights.pop(max_index)
            per_units.pop(max_index)
            values.pop (max_index)
        else:
            value += per_units[max_index] * capacity
            capacity = 0

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
