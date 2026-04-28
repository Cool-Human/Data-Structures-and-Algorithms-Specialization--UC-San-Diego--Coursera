from sys import stdin


def partition3(values):
    total = sum(values)
    
    if total % 3 != 0:
        return 0
    
    target = total // 3
    n = len(values)
    
    # dp = set of (sum1, sum2)
    dp = {(0, 0)}
    
    for value in values:
        new_dp = set(dp)
        for s1, s2 in dp:
            # Try putting in subset 1
            if s1 + value <= target:
                new_dp.add((s1 + value, s2))
            
            # Try putting in subset 2
            if s2 + value <= target:
                new_dp.add((s1, s2 + value))
        
        dp = new_dp
    
    return 1 if (target, target) in dp else 0


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))