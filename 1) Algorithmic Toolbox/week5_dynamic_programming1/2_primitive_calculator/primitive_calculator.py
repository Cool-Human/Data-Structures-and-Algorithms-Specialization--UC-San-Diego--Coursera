def compute_operations(n):
    memo, parent = [0] * (n + 1), [0] * (n + 1)

    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + 1
        parent[i] = i - 1

        if i % 2 == 0 and memo[i // 2] + 1 < memo[i]:
            memo[i] = memo[i // 2] + 1
            parent[i] = i // 2

        if i % 3 == 0 and memo[i // 3] + 1 < memo[i]:
            memo[i] = memo[i // 3] + 1
            parent[i] = i // 3
    
    pointer = n
    path = [n]
    
    while pointer:
        path.append(parent[pointer])
        pointer = parent[pointer]
    
    path.pop(-1)

    return path[::-1]
        


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence)-1)
    print(*output_sequence)