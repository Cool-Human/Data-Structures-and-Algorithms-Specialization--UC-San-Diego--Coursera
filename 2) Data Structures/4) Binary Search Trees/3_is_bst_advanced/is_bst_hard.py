# python3

import sys


def is_bst(tree):
    if not tree:
        return True

    # (node, low, low_inclusive, high, high_inclusive)
    stack = [(0, None, True, None, True)]

    while stack:
        node, low, low_inc, high, high_inc = stack.pop()

        key, left, right = tree[node]

        if low is not None:
            if low_inc:
                if key < low:
                    return False
            else:
                if key <= low:
                    return False

        if high is not None:
            if high_inc:
                if key > high:
                    return False
            else:
                if key >= high:
                    return False

        # Right subtree: keys >= current key
        if right != -1:
            stack.append((right, key, True, high, high_inc))

        # Left subtree: keys < current key
        if left != -1:
            stack.append((left, low, low_inc, key, False))

    return True


def main():
    n = int(sys.stdin.readline())

    tree = []
    for _ in range(n):
        key, left, right = map(int, sys.stdin.readline().split())
        tree.append((key, left, right))

    print("CORRECT" if is_bst(tree) else "INCORRECT")


if __name__ == "__main__":
    main()