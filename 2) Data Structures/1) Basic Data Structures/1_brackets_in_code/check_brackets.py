# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = []

    for i, ch in enumerate(text):
        pos = i + 1  # 1-based index

        if ch in "([{":
            stack.append(Bracket(ch, pos))

        elif ch in ")]}":
            if not stack:
                return pos

            top = stack.pop()

            if not are_matching(top.char, ch):
                return pos

    if stack:
        return stack[0].position  # first unmatched opening

    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()