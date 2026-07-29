from collections import Counter
from math import factorial

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        mid = ""
        half = []

        for c in sorted(cnt):
            if cnt[c] % 2:
                mid = c
            half.extend([c] * (cnt[c] // 2))

        freq = Counter(half)
        m = len(half)

        # initial number of permutations
        ways = factorial(m)
        for v in freq.values():
            ways //= factorial(v)

        if ways < k:
            return ""

        ans = []

        while m:
            for c in sorted(freq):
                if freq[c] == 0:
                    continue

                nxt = ways * freq[c] // m

                if nxt >= k:
                    ans.append(c)
                    ways = nxt
                    freq[c] -= 1
                    m -= 1
                    break
                else:
                    k -= nxt

        left = "".join(ans)
        return left + mid + left[::-1]