class Solution:
    def smallestNumber(self, num: str, t: int) -> str:

        # Factorize t
        need = [0, 0, 0, 0]   # powers of 2,3,5,7
        primes = [2, 3, 5, 7]

        for i, p in enumerate(primes):
            while t % p == 0:
                need[i] += 1
                t //= p

        # If any other prime remains
        if t != 1:
            return "-1"

        # Digit -> powers of 2,3,5,7
        factors = [
            (0, 0, 0, 0),  # 0
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0)   # 9
        ]

        A = need[0]
        B = need[1]

        INF = 10**9

        # dp[a][b] = minimum number of digits needed
        # to create 2^a * 3^b
        dp = [[INF] * (B + 1) for _ in range(A + 1)]
        best = [[""] * (B + 1) for _ in range(A + 1)]

        dp[0][0] = 0

        digits = [2, 3, 4, 6, 8, 9]

        for a in range(A + 1):
            for b in range(B + 1):

                if dp[a][b] == INF:
                    continue

                for d in digits:

                    fa, fb, _, _ = factors[d]

                    na = min(A, a + fa)
                    nb = min(B, b + fb)

                    new_count = dp[a][b] + 1
                    new_string = best[a][b] + str(d)

                    if new_count < dp[na][nb]:
                        dp[na][nb] = new_count
                        best[na][nb] = new_string

                    elif new_count == dp[na][nb]:
                        if new_string < best[na][nb]:
                            best[na][nb] = new_string

        # Construct smallest suffix
        def build(required, length):

            a, b, c, d = required

            # 5 and 7 each need one digit
            if c + d > length:
                return None

            if dp[a][b] == INF:
                return None

            used = dp[a][b] + c + d

            if used > length:
                return None

            result = best[a][b]

            result += "5" * c
            result += "7" * d

            # Remaining positions can be 1
            result += "1" * (length - used)

            # Arrange digits smallest first
            return "".join(sorted(result))

        n = len(num)

        # ------------------------------------------------
        # Check if num itself is valid
        # ------------------------------------------------

        if '0' not in num:

            current = [0, 0, 0, 0]

            for ch in num:
                f = factors[int(ch)]

                for j in range(4):
                    current[j] += f[j]

            if all(current[j] >= need[j] for j in range(4)):
                return num

        # ------------------------------------------------
        # Prefix factor counts
        # ------------------------------------------------

        pref = [[0, 0, 0, 0] for _ in range(n + 1)]

        for i, ch in enumerate(num):

            f = factors[int(ch)]

            for j in range(4):
                pref[i + 1][j] = pref[i][j] + f[j]

        # ------------------------------------------------
        # Try to make same-length answer
        # ------------------------------------------------

        for i in range(n - 1, -1, -1):

            # Prefix cannot contain zero
            if '0' in num[:i]:
                continue

            current_digit = int(num[i])

            # Try next larger digit
            for new_digit in range(current_digit + 1, 10):

                f = factors[new_digit]

                required = []

                for j in range(4):
                    remaining = need[j] - pref[i][j] - f[j]
                    required.append(max(0, remaining))

                suffix_length = n - i - 1

                suffix = build(required, suffix_length)

                if suffix is not None:
                    return num[:i] + str(new_digit) + suffix

        # ------------------------------------------------
        # No same-length answer.
        # Try ALL larger lengths
        # ------------------------------------------------

        for length in range(n + 1, n + 100):

            ans = build(need, length)

            if ans is not None:
                return ans

        return "-1"