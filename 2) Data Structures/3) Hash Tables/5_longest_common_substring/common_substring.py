# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

def solve(s, t):
	m1 = 1000000007
	m2 = 1000000009
	x = 263

	ns, nt = len(s), len(t)
	n = max(ns, nt)

	p1 = [1] * (n + 1)
	p2 = [1] * (n + 1)
	for i in range(1, n + 1):
		p1[i] = (p1[i - 1] * x) % m1
		p2[i] = (p2[i - 1] * x) % m2

	hs1 = [0] * (ns + 1)
	hs2 = [0] * (ns + 1)
	for i in range(ns):
		hs1[i + 1] = (hs1[i] * x + ord(s[i])) % m1
		hs2[i + 1] = (hs2[i] * x + ord(s[i])) % m2

	ht1 = [0] * (nt + 1)
	ht2 = [0] * (nt + 1)
	for i in range(nt):
		ht1[i + 1] = (ht1[i] * x + ord(t[i])) % m1
		ht2[i + 1] = (ht2[i] * x + ord(t[i])) % m2

	def get_hash(h1, h2, p1, p2, mod1, mod2, start, length):
		a = (h1[start + length] - h1[start] * p1[length]) % mod1
		b = (h2[start + length] - h2[start] * p2[length]) % mod2
		return (a, b)

	def check(length):
		if length == 0:
			return (0, 0)

		hashes = {}

		for i in range(ns - length + 1):
			h = get_hash(
				hs1, hs2, p1, p2,
				m1, m2, i, length
			)
			hashes[h] = i

		for j in range(nt - length + 1):
			h = get_hash(
				ht1, ht2, p1, p2,
				m1, m2, j, length
			)
			if h in hashes:
				return (hashes[h], j)

		return None

	low, high = 0, min(ns, nt)
	best_i = best_j = best_len = 0

	while low <= high:
		mid = (low + high) // 2
		res = check(mid)

		if res is not None:
			best_i, best_j = res
			best_len = mid
			low = mid + 1
		else:
			high = mid - 1

	return Answer(best_i, best_j, best_len)

for line in sys.stdin.readlines():
	s, t = line.split()
	ans = solve(s, t)
	print(ans.i, ans.j, ans.len)