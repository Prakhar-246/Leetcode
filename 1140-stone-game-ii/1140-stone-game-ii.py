class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = sum of piles[i:]
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dp(i, M):
            # All piles can be taken
            if i >= n:
                return 0

            if 2 * M >= n - i:
                return suffix[i]

            # Already calculated
            if (i, M) in memo:
                return memo[(i, M)]

            # Opponent will try to minimize our result
            opponent = float('inf')

            for X in range(1, 2 * M + 1):

                next_M = max(M, X)

                opponent = min(
                    opponent,
                    dp(i + X, next_M)
                )

            # Current player gets everything except
            # what the opponent can get.
            memo[(i, M)] = suffix[i] - opponent

            return memo[(i, M)]

        return dp(0, 1)