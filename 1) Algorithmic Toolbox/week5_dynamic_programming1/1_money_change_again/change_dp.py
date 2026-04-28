def change(money):
    change = [1, 3, 4]
    dp = [float('inf')] * (money + 1)
    dp[0] = 0
    for i in change:
        for j in range(i, money + 1):
            dp[j] = min(dp[j], dp[j - i] + 1)

    return dp[money] if dp[money] != float('inf') else -1


if __name__ == '__main__':
    m = int(input())
    print(change(m))