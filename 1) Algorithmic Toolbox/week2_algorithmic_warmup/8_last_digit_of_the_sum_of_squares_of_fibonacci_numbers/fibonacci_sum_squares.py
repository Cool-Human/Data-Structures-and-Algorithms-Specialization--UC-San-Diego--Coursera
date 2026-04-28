def fib_last_digit(k):
    if k <= 1:
        return k
    a, b = 0, 1
    for _ in range(2, k + 1):
        a, b = b, (a + b) % 10
    return b

def fibonacci_sum_squares(n):
    if n <= 1:
        return n
    fn = fib_last_digit(n % 60)
    fn1 = fib_last_digit((n + 1) % 60)
    return (fn * fn1) % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
