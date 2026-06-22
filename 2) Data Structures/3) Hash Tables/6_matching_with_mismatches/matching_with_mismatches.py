# python3

import sys

def solve(k, text, pattern):
	n = len(text)
	m = len(pattern)

	if m > n:
		return []

	mod1 = 1000000007
	mod2 = 1000000009
	x = 263

	L = max(n, m)

	pow1 = [1] * (L + 1)
	pow2 = [1] * (L + 1)
	for i in range(1, L + 1):
		pow1[i] = (pow1[i - 1] * x) % mod1
		pow2[i] = (pow2[i - 1] * x) % mod2

	def build_hash(s, mod):
		h = [0] * (len(s) + 1)
		for i, c in enumerate(s):
			h[i + 1] = (h[i] * x + ord(c)) % mod
		return h

	ht1 = build_hash(text, mod1)
	ht2 = build_hash(text, mod2)
	hp1 = build_hash(pattern, mod1)
	hp2 = build_hash(pattern, mod2)

	def get_hash(h, start, length, pw, mod):
		return (h[start + length] - h[start] * pw[length]) % mod

	def equal(ts, ps, length):
		return (
			get_hash(ht1, ts, length, pow1, mod1) ==
			get_hash(hp1, ps, length, pow1, mod1)
			and
			get_hash(ht2, ts, length, pow2, mod2) ==
			get_hash(hp2, ps, length, pow2, mod2)
		)

	def mismatches(start):
		cnt = 0
		pos = 0

		while pos < m and cnt <= k:
			lo, hi = 0, m - pos

			while lo < hi:
				mid = (lo + hi + 1) // 2
				if equal(start + pos, pos, mid):
					lo = mid
				else:
					hi = mid - 1

			match_len = lo
			pos += match_len

			if pos < m:
				cnt += 1
				pos += 1

		return cnt

	ans = []

	for i in range(n - m + 1):
		if mismatches(i) <= k:
			ans.append(i)

	return ans

for line in sys.stdin.readlines():
	k, t, p = line.split()
	ans = solve(int(k), t, p)
	print(len(ans), *ans)