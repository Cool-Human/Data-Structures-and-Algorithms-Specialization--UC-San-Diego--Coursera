def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def maximum_value(dataset):
    # Split numbers and operators
    nums = list(map(int, dataset[::2]))
    ops = list(dataset[1::2])
    n = len(nums)

    # DP tables
    min_dp = [[0] * n for _ in range(n)]
    max_dp = [[0] * n for _ in range(n)]

    # Base case
    for i in range(n):
        min_dp[i][i] = nums[i]
        max_dp[i][i] = nums[i]

    # Fill DP
    for s in range(1, n):  # length - 1
        for i in range(n - s):
            j = i + s

            min_val = float('inf')
            max_val = float('-inf')

            for k in range(i, j):
                op = ops[k]

                a = evaluate(max_dp[i][k], max_dp[k+1][j], op)
                b = evaluate(max_dp[i][k], min_dp[k+1][j], op)
                c = evaluate(min_dp[i][k], max_dp[k+1][j], op)
                d = evaluate(min_dp[i][k], min_dp[k+1][j], op)

                min_val = min(min_val, a, b, c, d)
                max_val = max(max_val, a, b, c, d)

            min_dp[i][j] = min_val
            max_dp[i][j] = max_val

    return max_dp[0][n-1]


if __name__ == "__main__":
    print(maximum_value(input()))
