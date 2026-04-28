def get_pisano_period(m):
    if m == 1:
        return 1
    previous, current = 0, 1
    for i in range(1, m * m + 1):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i
    return 0

def fibonacci_huge(n, m):
    if n <= 1:
        return n % m
    period = get_pisano_period(m)
    n = n % period
    if n <= 1:
        return n % m
    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, (previous + current) % m
    return current


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))
