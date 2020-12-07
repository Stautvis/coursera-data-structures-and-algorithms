# Uses python3
import sys

def partition3(A):
    if len(A) < 3: return 0 # if less then 3 elements

    sum_of_elements = sum (A)
    if sum_of_elements % 3 != 0: return 0 # if cannot to divide in tree equal subsets
    sum_of_sets = sum_of_elements / 3

    return subsetSum(A, len(A) - 1, sum_of_sets, sum_of_sets, sum_of_sets)

def subsetSum(elements, n, a, b, c, previous_sets = {}):
    if a == 0 and b == 0 and c == 0: # if all sets equal to zero
        return True
    if len(elements) < 0: # if no elements left
        return False

    key = (a, b, c, n)
    if key not in previous_sets:
        A = False
        if a - elements[n] >= 0:
            A = subsetSum(elements, n - 1, a - elements[n], b, c, previous_sets)
        B = False
        if not A and (b - elements[n] >= 0):
            B = subsetSum(elements, n - 1, a, b - elements[n], c, previous_sets)
        C = False
        if not A and not B and (c - elements[n] >= 0):
            C = subsetSum(elements, n - 1, a, b, c - elements[n], previous_sets)

        previous_sets[key] = A or B or C
    return previous_sets[key]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    
    if partition3(A): print(1)
    else: print(0)

