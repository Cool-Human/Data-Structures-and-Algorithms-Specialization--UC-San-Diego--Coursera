def lcs3(A, B, C):
    n, m, p = len(A), len(B), len(C)
    
    # 3D DP array
    dp = [[[0] * (p + 1) for _ in range(m + 1)] for __ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, p + 1):
                if A[i - 1] == B[j - 1] == C[k - 1]:
                    dp[i][j][k] = 1 + dp[i - 1][j - 1][k - 1]
                else:
                    dp[i][j][k] = max(
                        dp[i - 1][j][k],
                        dp[i][j - 1][k],
                        dp[i][j][k - 1]
                    )
    
    return dp[n][m][p]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))