# python3

from collections import deque

def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))
    return maximums

def max_faster(sequence, m):
    dq = deque()
    max_values = []

    for i in range(len(sequence)):
        while dq and dq[0] <= i - m:
            dq.popleft()
        
        while dq and sequence[dq[-1]] <= sequence[i]:
            dq.pop()
        
        dq. append(i)

        if i >= m - 1:
            max_values.append(sequence[dq[0]])
    
    return max_values

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    # print(*max_sliding_window_naive(input_sequence, window_size))

    print(*max_faster(input_sequence, window_size))