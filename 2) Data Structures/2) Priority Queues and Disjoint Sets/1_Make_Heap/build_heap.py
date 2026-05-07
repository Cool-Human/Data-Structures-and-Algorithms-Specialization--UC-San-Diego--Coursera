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
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps

def build_heap_fast(data):
    """Build a min-heap from data inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    swaps_new = []
    n = len(data)

    def sift_down(i):
        min_index = i

        left = 2 * i + 1
        if left < n and data[left] < data[min_index]:
            min_index = left

        right = 2 * i + 2
        if right < n and data[right] < data[min_index]:
            min_index = right

        if i != min_index:
            swaps_new.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]
            sift_down(min_index)

    # Start from the last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        sift_down(i)

    return swaps_new


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    # swaps = build_heap(data)

    # print(len(swaps))
    # for i, j in swaps:
    #     print(i, j)
    
    swaps_new = build_heap_fast(data)
    print(len(swaps_new))
    for i,j in swaps_new:
        print(i, j)

if __name__ == "__main__":
    main()