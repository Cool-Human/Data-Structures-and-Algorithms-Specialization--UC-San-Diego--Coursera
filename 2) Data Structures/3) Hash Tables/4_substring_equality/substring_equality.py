# python3

import sys

class Solver:
	def __init__(self, s):
		self.s = s.rstrip()

		self.m1 = 1000000007
		self.m2 = 1000000009
		self.x = 263

		n = len(self.s)

		self.h1 = [0] * (n + 1)
		self.h2 = [0] * (n + 1)
		self.p1 = [1] * (n + 1)
		self.p2 = [1] * (n + 1)

		for i in range(1, n + 1):
			c = ord(self.s[i - 1])

			self.h1[i] = (self.h1[i - 1] * self.x + c) % self.m1
			self.h2[i] = (self.h2[i - 1] * self.x + c) % self.m2

			self.p1[i] = (self.p1[i - 1] * self.x) % self.m1
			self.p2[i] = (self.p2[i - 1] * self.x) % self.m2

	def _hash(self, a, l, h, p, m):
		return (h[a + l] - p[l] * h[a]) % m

	def ask(self, a, b, l):
		return (
			self._hash(a, l, self.h1, self.p1, self.m1) ==
			self._hash(b, l, self.h1, self.p1, self.m1)
			and
			self._hash(a, l, self.h2, self.p2, self.m2) ==
			self._hash(b, l, self.h2, self.p2, self.m2)
		)

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")