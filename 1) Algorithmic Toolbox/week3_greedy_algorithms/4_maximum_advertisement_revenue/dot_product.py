from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    # Sort both sequences in descending order to maximize the dot product
    first_sorted = sorted(first_sequence, reverse=True)
    second_sorted = sorted(second_sequence, reverse=True)
    return sum(a * b for a, b in zip(first_sorted, second_sorted))


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))