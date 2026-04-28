# Uses python3
import sys

def fib_last_digit(k):
    if k <= 1:
        return k
    a, b = 0, 1
    for _ in range(2, k + 1):
        a, b = b, (a + b) % 10
    return b

def fibonacci_partial_sum(from_, to):
    if from_ > to:
        return 0
    s_n = fib_last_digit((to + 2) % 60)
    s_m1 = fib_last_digit((from_ + 1) % 60) if from_ >= 1 else 0
    return (s_n - s_m1) % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
