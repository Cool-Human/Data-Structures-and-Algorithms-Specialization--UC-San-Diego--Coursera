# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 1000000007
    x = 263

    m = len(pattern)
    n = len(text)

    if m > n:
        return []

    def poly_hash(s):
        h = 0
        for c in reversed(s):
            h = (h * x + ord(c)) % p
        return h

    p_hash = poly_hash(pattern)

    H = [0] * (n - m + 1)
    H[-1] = poly_hash(text[n - m:])

    y = pow(x, m, p)

    for i in range(n - m - 1, -1, -1):
        H[i] = (
            (x * H[i + 1] + ord(text[i]) - y * ord(text[i + m]))
            % p
        )

    result = []
    for i in range(n - m + 1):
        if H[i] == p_hash and text[i:i + m] == pattern:
            result.append(i)

    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))