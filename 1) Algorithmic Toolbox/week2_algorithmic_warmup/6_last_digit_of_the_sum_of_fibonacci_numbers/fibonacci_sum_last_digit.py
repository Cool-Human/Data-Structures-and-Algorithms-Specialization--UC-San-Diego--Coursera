def fib_last_digit(k):
    if k <= 1:
        return k
    a, b = 0, 1
    for _ in range(2, k + 1):
        a, b = b, (a + b) % 10
    return b

def fibonacci_sum(n):
    if n < 0:
        return 0
    k = (n + 2) % 60
    f = fib_last_digit(k)
    return (f - 1) % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
