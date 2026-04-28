def binary_search(keys, query):
    left = 0
    right = len(keys) - 1
    while left <= right:
        middle = left + (right -left) // 2
        if keys[middle] == query:
            return middle
        elif keys[middle] > query:
            right = middle -1
        else:
            left = middle + 1
    return -1



if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
