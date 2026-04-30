import sys
from collections import deque

input = sys.stdin.readline

def compute_height(n, parents):
    children = [[] for _ in range(n)]
    root = -1

    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            children[parents[i]].append(i)

    queue = deque([root])
    height = 0

    while queue:
        height += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            queue.extend(children[node])

    return height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


if __name__ == "__main__":
    main()