def binary_search(keys, query):
    left, right = 0, len(keys) - 1
    result = -1
    while left <= right:
        middle = (left + right) // 2
        if keys[middle] == query:
            result = middle
            right = middle - 1  # Continue searching left for earlier occurrence
        elif keys[middle] < query:
            left = middle + 1
        else:
            right = middle - 1
    return result


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
