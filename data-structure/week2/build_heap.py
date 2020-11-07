# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []

    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        shift_up(data, i, swaps)
    return swaps

def shift_up(data, i, swaps):
    n = len(data)
    p = i # root
    l = 2 * i + 1# left
    r = 2 * i + 2 # right
  
    if l < n and data[l] < data[p]: 
        p = l
    if r < n and data[r] < data[p]: 
        p = r;

    if p != i:
        swaps.append((i, p))
        data[i], data[p] = data[p], data[i]; 
        shift_up(data, p, swaps); 


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
