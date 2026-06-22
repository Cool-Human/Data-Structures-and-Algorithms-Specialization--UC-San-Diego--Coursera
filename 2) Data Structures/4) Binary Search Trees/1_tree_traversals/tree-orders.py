# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0] * self.n
        self.left = [0] * self.n
        self.right = [0] * self.n

        for i in range(self.n):
            a, b, c = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        result = []

        def traverse(v):
            if v == -1:
                return
            traverse(self.left[v])
            result.append(self.key[v])
            traverse(self.right[v])

        if self.n > 0:
            traverse(0)
        return result

    def preOrder(self):
        result = []

        def traverse(v):
            if v == -1:
                return
            result.append(self.key[v])
            traverse(self.left[v])
            traverse(self.right[v])

        if self.n > 0:
            traverse(0)
        return result

    def postOrder(self):
        result = []

        def traverse(v):
            if v == -1:
                return
            traverse(self.left[v])
            traverse(self.right[v])
            result.append(self.key[v])

        if self.n > 0:
            traverse(0)
        return result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()