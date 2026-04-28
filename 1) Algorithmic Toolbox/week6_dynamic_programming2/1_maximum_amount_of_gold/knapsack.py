from sys import stdin


def maximum_gold(capacity, weights):
    dp = [0] * (capacity + 1)

    for weight in weights:
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + weight)

    return dp[capacity]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
