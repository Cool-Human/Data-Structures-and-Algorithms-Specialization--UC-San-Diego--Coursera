# python3

import sys
import threading

sys.setrecursionlimit(10**7)
threading.stack_size(2**25)


def IsBinarySearchTree(tree):
    if not tree:
        return True

    def check(node, low, high):
        if node == -1:
            return True

        key, left, right = tree[node]

        if key <= low or key >= high:
            return False

        return (
            check(left, low, key) and
            check(right, key, high)
        )

    return check(0, float('-inf'), float('inf'))


def main():
    n = int(sys.stdin.readline())

    tree = []
    for _ in range(n):
        key, left, right = map(int, sys.stdin.readline().split())
        tree.append((key, left, right))

    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()